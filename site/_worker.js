export default {
  async fetch(request, env) {
    const authHeader = request.headers.get('Authorization');

    if (!authHeader) {
      return new Response('Unauthorized', {
        status: 401,
        headers: {
          'WWW-Authenticate': 'Basic realm="Password required"'
        }
      });
    }

    const base64Credentials = authHeader.split(' ')[1];
    try {
      const credentials = atob(base64Credentials);
      const [username, password] = credentials.split(':');

      // Allow if the password matches, regardless of the username.
      if (password === 'munverricht1989') {
        return env.ASSETS.fetch(request);
      }
    } catch (e) {}

    return new Response('Unauthorized', {
      status: 401,
      headers: {
        'WWW-Authenticate': 'Basic realm="Password required"'
      }
    });
  }
};
