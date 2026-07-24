from __future__ import annotations

from pathlib import Path
from typing import Tuple

from PIL import Image, ImageEnhance, ImageOps, ImageDraw, ImageFilter, ImageFont
from reportlab.graphics import renderPDF
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from svglib.svglib import svg2rlg


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "output" / "pdf"
TMP_DIR = ROOT / "tmp" / "pdfs"
PDF_PATH = OUTPUT_DIR / "Joelle_Mila_Agility-Auszeit_A4.pdf"
PREVIEW_PATH = OUTPUT_DIR / "Joelle_Mila_Agility-Auszeit_Vorschau.png"

ACTION_PHOTO = ROOT / "WhatsApp Image 2026-07-23 at 14.58.31.jpeg"
MILA_PHOTO = ROOT / "IMG_4759.JPEG"
BOOKING_URL = "https://hsz-luenen-brambauer.de/buchen/"
LUCIDE_DIR = ROOT / "assets" / "lucide"
PAW_SVG = LUCIDE_DIR / "paw-print.svg"
BONE_SVG = LUCIDE_DIR / "bone.svg"
DOG_SVG = LUCIDE_DIR / "dog.svg"

PAGE_W, PAGE_H = A4
PANEL_H = PAGE_H / 2

CREAM = HexColor("#F7F1E6")
CREAM_DARK = HexColor("#E9DDC9")
FOREST = HexColor("#23483A")
FOREST_DARK = HexColor("#17342A")
SAGE = HexColor("#DDE7DD")
SAGE_DARK = HexColor("#A7B8A8")
GOLD = HexColor("#D4A34B")
GOLD_LIGHT = HexColor("#F1E2BC")
INK = HexColor("#26342E")
WHITE = HexColor("#FFFFFF")

FONT_REGULAR = "SegoeUI"
FONT_BOLD = "SegoeUI-Bold"
FONT_TITLE = "Trebuchet-Bold"
FONT_SERIF_BOLD = "Georgia-Bold"


def register_fonts() -> None:
    fonts = {
        FONT_REGULAR: Path(r"C:\Windows\Fonts\segoeui.ttf"),
        FONT_BOLD: Path(r"C:\Windows\Fonts\segoeuib.ttf"),
        FONT_TITLE: Path(r"C:\Windows\Fonts\trebucbd.ttf"),
        FONT_SERIF_BOLD: Path(r"C:\Windows\Fonts\georgiab.ttf"),
    }
    for name, path in fonts.items():
        if not path.exists():
            raise FileNotFoundError(f"Schrift fehlt: {path}")
        pdfmetrics.registerFont(TTFont(name, str(path)))


def prepare_photo(
    path: Path,
    box_ratio: float,
    max_width_px: int,
    centering: Tuple[float, float] = (0.5, 0.5),
    pre_crop: Tuple[float, float, float, float] | None = None,
    contrast: float = 1.02,
    color: float = 1.02,
) -> Image.Image:
    image = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    if pre_crop:
        left, top, right, bottom = pre_crop
        image = image.crop(
            (
                round(image.width * left),
                round(image.height * top),
                round(image.width * right),
                round(image.height * bottom),
            )
        )
    target_width = min(max_width_px, image.width)
    target_height = max(1, round(target_width / box_ratio))
    if target_height > image.height:
        target_height = image.height
        target_width = max(1, round(target_height * box_ratio))
    image = ImageOps.fit(
        image,
        (target_width, target_height),
        method=Image.Resampling.LANCZOS,
        centering=centering,
    )
    image = ImageEnhance.Contrast(image).enhance(contrast)
    return ImageEnhance.Color(image).enhance(color)


def draw_rounded_photo(
    c: canvas.Canvas,
    image: Image.Image,
    x: float,
    y: float,
    width: float,
    height: float,
    radius: float,
    border_color=GOLD,
    border_width: float = 1.0,
) -> None:
    c.saveState()
    clip = c.beginPath()
    clip.roundRect(x, y, width, height, radius)
    c.clipPath(clip, stroke=0, fill=0)
    c.drawImage(
        ImageReader(image),
        x,
        y,
        width,
        height,
        preserveAspectRatio=False,
        mask="auto",
    )
    c.restoreState()
    c.setStrokeColor(border_color)
    c.setLineWidth(border_width)
    c.roundRect(x, y, width, height, radius, stroke=1, fill=0)


def draw_svg_icon(
    c: canvas.Canvas,
    path: Path,
    x: float,
    y: float,
    size: float,
    color=FOREST,
    alpha: float = 1.0,
    rotation: float = 0,
) -> None:
    drawing = svg2rlg(str(path))
    if drawing is None:
        raise ValueError(f"SVG konnte nicht gelesen werden: {path}")

    def recolor(node) -> None:
        if hasattr(node, "strokeWidth") and node.strokeWidth is not None:
            node.strokeColor = color
            node.strokeOpacity = alpha
            node.strokeWidth = 1.7
        if hasattr(node, "contents"):
            for child in node.contents:
                recolor(child)

    recolor(drawing)
    scale = size / max(drawing.width, drawing.height)
    c.saveState()
    c.translate(x, y)
    c.rotate(rotation)
    c.scale(scale, scale)
    renderPDF.draw(drawing, c, -drawing.width / 2, -drawing.height / 2)
    c.restoreState()


def draw_fold_ticks(c: canvas.Canvas) -> None:
    c.saveState()
    c.setStrokeColor(SAGE_DARK)
    c.setLineWidth(0.45)
    c.setDash(1.4, 1.4)
    c.line(4 * mm, PANEL_H, 10 * mm, PANEL_H)
    c.line(PAGE_W - 10 * mm, PANEL_H, PAGE_W - 4 * mm, PANEL_H)
    c.restoreState()


def draw_paragraph(
    c: canvas.Canvas,
    text: str,
    style: ParagraphStyle,
    x: float,
    y: float,
    width: float,
    height: float,
) -> Tuple[float, float]:
    paragraph = Paragraph(text, style)
    used_width, used_height = paragraph.wrap(width, height)
    paragraph.drawOn(c, x, y + height - used_height)
    return used_width, used_height


def draw_qr(c: canvas.Canvas, x: float, y: float, size: float) -> None:
    qr = QrCodeWidget(BOOKING_URL, barLevel="M")
    x1, y1, x2, y2 = qr.getBounds()
    width = x2 - x1
    height = y2 - y1
    drawing = Drawing(
        size,
        size,
        transform=[size / width, 0, 0, size / height, 0, 0],
    )
    drawing.add(qr)
    renderPDF.draw(drawing, c, x, y)
    c.linkURL(BOOKING_URL, (x, y, x + size, y + size), relative=0)


def draw_cover(c: canvas.Canvas, action_image: Image.Image) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PANEL_H, stroke=0, fill=1)

    photo_x = 8.5 * mm
    photo_y = 35.5 * mm
    photo_w = PAGE_W - 17 * mm
    photo_h = PANEL_H - 43.5 * mm
    draw_rounded_photo(c, action_image, photo_x, photo_y, photo_w, photo_h, 4 * mm)

    c.setFillColor(FOREST)
    c.setFont(FONT_TITLE, 17.5)
    c.drawCentredString(PAGE_W / 2, 22.5 * mm, "HÜPFEN. LACHEN. LECKERLI!")

    c.setFillColor(INK)
    c.setFont(FONT_REGULAR, 10.2)
    c.drawCentredString(
        PAGE_W / 2,
        13.5 * mm,
        "Eine kleine Agility-Auszeit für Joelle & Mila",
    )

    c.setStrokeColor(GOLD)
    c.setLineWidth(1.8)
    c.line(PAGE_W / 2 - 22 * mm, 9.3 * mm, PAGE_W / 2 + 22 * mm, 9.3 * mm)


def draw_back_cover_upright(c: canvas.Canvas) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PANEL_H, stroke=0, fill=1)
    c.setFillColor(SAGE)
    c.circle(PAGE_W / 2, PANEL_H / 2 + 10 * mm, 25 * mm, fill=1, stroke=0)
    draw_svg_icon(
        c,
        DOG_SVG,
        PAGE_W / 2,
        PANEL_H / 2 + 10 * mm,
        29 * mm,
        FOREST,
        alpha=0.94,
    )

    c.setFillColor(FOREST)
    c.setFont(FONT_SERIF_BOLD, 15)
    c.drawCentredString(PAGE_W / 2, PANEL_H / 2 - 21 * mm, "Joelle & Mila")
    c.setFillColor(INK)
    c.setFont(FONT_REGULAR, 9.5)
    c.drawCentredString(PAGE_W / 2, PANEL_H / 2 - 29 * mm, "Hauptsache zusammen.")
    c.setFillColor(SAGE_DARK)
    c.setFont(FONT_REGULAR, 5.2)
    c.drawCentredString(PAGE_W / 2, 9 * mm, "Icons: Lucide · ISC License")


def draw_outer_page(c: canvas.Canvas, action_image: Image.Image) -> None:
    # Obere Hälfte: Rückseite. Sie steht auf dem flachen Druckbogen absichtlich kopfüber.
    c.saveState()
    c.translate(PAGE_W, PAGE_H)
    c.rotate(180)
    draw_back_cover_upright(c)
    c.restoreState()

    # Untere Hälfte: Vorderseite, auf dem Druckbogen normal lesbar.
    draw_cover(c, action_image)
    draw_fold_ticks(c)


def draw_speech_bubble(c: canvas.Canvas, x: float, y: float, w: float, h: float) -> None:
    c.saveState()
    c.setFillColor(WHITE)
    c.setStrokeColor(CREAM_DARK)
    c.setLineWidth(0.9)
    c.roundRect(x, y, w, h, 7 * mm, stroke=1, fill=1)
    tail = c.beginPath()
    tail.moveTo(x + 2 * mm, y + 27 * mm)
    tail.lineTo(x - 14 * mm, y + 18 * mm)
    tail.lineTo(x + 4 * mm, y + 12 * mm)
    tail.close()
    c.drawPath(tail, stroke=1, fill=1)
    c.restoreState()


def draw_inside_top(c: canvas.Canvas, mila_image: Image.Image) -> None:
    y0 = PANEL_H
    c.setFillColor(SAGE)
    c.rect(0, y0, PAGE_W, PANEL_H, stroke=0, fill=1)

    c.setFillColor(FOREST)
    c.setFont(FONT_BOLD, 9.5)
    c.drawString(13 * mm, PAGE_H - 13 * mm, "MILA HAT SCHON MAL VORGEPACKT ...")

    photo_x = 14 * mm
    photo_y = y0 + 16 * mm
    photo_w = 68 * mm
    photo_h = 108 * mm
    draw_rounded_photo(
        c,
        mila_image,
        photo_x,
        photo_y,
        photo_w,
        photo_h,
        4 * mm,
        border_color=WHITE,
        border_width=2.2,
    )

    bubble_x = 109 * mm
    bubble_y = y0 + 62 * mm
    bubble_w = 78 * mm
    bubble_h = 36 * mm
    draw_speech_bubble(c, bubble_x, bubble_y, bubble_w, bubble_h)

    bubble_style = ParagraphStyle(
        "bubble",
        fontName=FONT_TITLE,
        fontSize=16.5,
        leading=20,
        textColor=FOREST_DARK,
        alignment=TA_CENTER,
        spaceAfter=0,
    )
    bubble_text = (
        "Ich wäre dann<br/>bereit.<br/>"
        f'<font color="{GOLD.hexval()}">Leckerli auch?</font>'
    )
    draw_paragraph(
        c,
        bubble_text,
        bubble_style,
        bubble_x + 5 * mm,
        bubble_y + 4.5 * mm,
        bubble_w - 10 * mm,
        bubble_h - 9 * mm,
    )

    c.setFillColor(FOREST)
    c.setFont(FONT_REGULAR, 8.5)
    c.drawCentredString(
        bubble_x + bubble_w / 2,
        y0 + 52 * mm,
        "Mila, zuständig für die Leckerli-Kontrolle",
    )
    draw_svg_icon(
        c,
        PAW_SVG,
        PAGE_W - 25 * mm,
        y0 + 21 * mm,
        11 * mm,
        GOLD,
        alpha=0.78,
        rotation=12,
    )
    draw_svg_icon(
        c,
        BONE_SVG,
        PAGE_W - 11 * mm,
        y0 + 29 * mm,
        8 * mm,
        GOLD,
        alpha=0.55,
        rotation=-18,
    )


def draw_money_area(c: canvas.Canvas) -> None:
    box_x = 128 * mm
    box_y = 55 * mm
    box_w = 69 * mm
    box_h = 60 * mm

    c.saveState()
    c.setFillColor(GOLD_LIGHT)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.25)
    c.setDash(4, 3)
    c.roundRect(box_x, box_y, box_w, box_h, 4 * mm, stroke=1, fill=1)
    c.restoreState()

    c.setFillColor(FOREST)
    c.setFont(FONT_TITLE, 15.5)
    c.drawCentredString(box_x + box_w / 2, box_y + box_h - 15 * mm, "Spaßbudget")
    c.setFont(FONT_REGULAR, 9.4)
    c.drawCentredString(box_x + box_w / 2, box_y + box_h - 24 * mm, "für Joelle & Mila")

    c.setFillColor(INK)
    c.setFont(FONT_REGULAR, 7.4)
    c.drawCentredString(
        box_x + box_w / 2,
        box_y + 15 * mm,
        "Hier darf das Geld einziehen.",
    )
    c.setFillColor(FOREST)
    c.setFont(FONT_REGULAR, 6.8)
    c.drawCentredString(
        box_x + box_w / 2,
        box_y + 9 * mm,
        "Papierclip oder lösbares Klebeband genügt.",
    )
    draw_svg_icon(
        c,
        BONE_SVG,
        box_x + box_w - 11 * mm,
        box_y + 12 * mm,
        8 * mm,
        GOLD,
        alpha=0.72,
        rotation=-18,
    )


def draw_inside_bottom(c: canvas.Canvas) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PANEL_H, stroke=0, fill=1)

    # Große, ruhige Schreibfläche für den handschriftlichen Gruß.
    c.saveState()
    c.setFillColor(WHITE)
    c.setStrokeColor(CREAM_DARK)
    c.setLineWidth(0.8)
    c.roundRect(
        11 * mm,
        18 * mm,
        105 * mm,
        111 * mm,
        4 * mm,
        stroke=1,
        fill=1,
    )
    c.setStrokeColor(SAGE_DARK)
    c.setLineWidth(0.45)
    for line_y in (111, 96, 81, 66, 51, 36):
        c.line(
            17 * mm,
            line_y * mm,
            110 * mm,
            line_y * mm,
        )
    c.restoreState()
    draw_svg_icon(
        c,
        DOG_SVG,
        103 * mm,
        25 * mm,
        13 * mm,
        SAGE_DARK,
        alpha=0.36,
    )

    draw_money_area(c)

    qr_size = 18 * mm
    qr_x = 129 * mm
    qr_y = 14 * mm
    draw_qr(c, qr_x, qr_y, qr_size)
    c.setFillColor(FOREST)
    c.setFont(FONT_BOLD, 7.6)
    c.drawString(qr_x + qr_size + 5 * mm, qr_y + 12.5 * mm, "Wann ihr mögt.")
    c.setFillColor(INK)
    c.setFont(FONT_REGULAR, 7.1)
    c.drawString(
        qr_x + qr_size + 5 * mm,
        qr_y + 7.5 * mm,
        "Den Termin sucht ihr euch selbst aus.",
    )
    c.setFillColor(SAGE_DARK)
    c.setFont(FONT_REGULAR, 5.9)
    c.drawString(qr_x + qr_size + 5 * mm, qr_y + 2.5 * mm, "hsz-luenen-brambauer.de/buchen")
    c.linkURL(
        BOOKING_URL,
        (
            qr_x + qr_size + 5 * mm,
            qr_y,
            PAGE_W - 12 * mm,
            qr_y + 18 * mm,
        ),
        relative=0,
    )


def draw_inside_page(c: canvas.Canvas, mila_image: Image.Image) -> None:
    # Bei Duplexdruck "an langer Kante wenden":
    # obere Hälfte = Innenseite hinter dem Frontdeckel,
    # untere Hälfte = handschriftliche Grußfläche/Geldfläche.
    draw_inside_top(c, mila_image)
    draw_inside_bottom(c)
    draw_fold_ticks(c)


def build_pdf() -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    register_fonts()

    action_box_ratio = (PAGE_W - 17 * mm) / (PANEL_H - 43.5 * mm)
    action_image = prepare_photo(
        ACTION_PHOTO,
        action_box_ratio,
        max_width_px=1600,
        centering=(0.5, 0.50),
        contrast=1.04,
        color=1.03,
    )
    mila_box_ratio = (68 * mm) / (108 * mm)
    mila_image = prepare_photo(
        MILA_PHOTO,
        mila_box_ratio,
        max_width_px=900,
        centering=(0.5, 0.66),
        pre_crop=(0.0, 0.15, 1.0, 1.0),
        contrast=1.03,
        color=1.01,
    )

    c = canvas.Canvas(str(PDF_PATH), pagesize=A4, pageCompression=1)
    c.setTitle("Agility-Auszeit für Joelle & Mila")
    c.setSubject("Doppelseitige A4-Klappkarte zum Geburtstag")
    c.setAuthor("Geburtstagskarte für Joelle")
    c.setCreator("Codex - ReportLab")

    draw_outer_page(c, action_image)
    c.showPage()
    draw_inside_page(c, mila_image)
    c.showPage()
    c.save()
    return PDF_PATH


def rounded_paste(base: Image.Image, card: Image.Image, xy: Tuple[int, int], radius: int) -> None:
    mask = Image.new("L", card.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((0, 0, card.width - 1, card.height - 1), radius=radius, fill=255)
    shadow = Image.new("RGBA", (card.width + 50, card.height + 50), (0, 0, 0, 0))
    shadow_mask = Image.new("L", shadow.size, 0)
    shadow_draw = ImageDraw.Draw(shadow_mask)
    shadow_draw.rounded_rectangle((20, 20, card.width + 20, card.height + 20), radius=radius, fill=125)
    shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(13))
    shadow.putalpha(shadow_mask)
    base.paste(shadow, (xy[0] - 20, xy[1] - 20), shadow)
    base.paste(card, xy, mask)


def build_preview(page_one_path: Path, page_two_path: Path) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    page_one = Image.open(page_one_path).convert("RGB")
    page_two = Image.open(page_two_path).convert("RGB")

    front = page_one.crop((0, page_one.height // 2, page_one.width, page_one.height))
    inside = page_two

    canvas_width = 2200
    canvas_height = 1350
    preview = Image.new("RGB", (canvas_width, canvas_height), "#EEE8DE")
    draw = ImageDraw.Draw(preview)

    title_font = ImageFont.truetype(r"C:\Windows\Fonts\trebucbd.ttf", 56)
    label_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 26)
    note_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 23)
    draw.text((90, 55), "Agility-Auszeit für Joelle & Mila", font=title_font, fill="#23483A")

    front_target_w = 960
    front_target_h = round(front.height * front_target_w / front.width)
    front = front.resize((front_target_w, front_target_h), Image.Resampling.LANCZOS)
    inside_target_h = 1040
    inside_target_w = round(inside.width * inside_target_h / inside.height)
    inside = inside.resize((inside_target_w, inside_target_h), Image.Resampling.LANCZOS)

    front_xy = (90, 245)
    inside_xy = (1220, 190)
    rounded_paste(preview, front, front_xy, radius=22)
    rounded_paste(preview, inside, inside_xy, radius=18)

    draw.text((front_xy[0], 185), "Vorderseite (gefaltet)", font=label_font, fill="#26342E")
    draw.text((inside_xy[0], 130), "Innenseite (aufgeklappt)", font=label_font, fill="#26342E")
    draw.text(
        (90, 1190),
        "Drucken: A4 · 100 % / Tatsächliche Größe · beidseitig · an langer Kante wenden",
        font=note_font,
        fill="#5B6A62",
    )
    draw.text(
        (90, 1235),
        "Danach an den kleinen seitlichen Markierungen mittig falten.",
        font=note_font,
        fill="#5B6A62",
    )

    preview.save(PREVIEW_PATH, quality=95)
    return PREVIEW_PATH


if __name__ == "__main__":
    print(build_pdf())
