const jsonServer = require('json-server')
const server = jsonServer.create()
const router = jsonServer.router(require('./db.js')())

server.use(jsonServer.defaults())

const middlewares = jsonServer.defaults()
// Set default middlewares (logger, static, cors and no-cache)
server.use(middlewares)

// server.use(jsonServer.rewriter({
//   '/api/*': '/$1',
//   '/blog/:resource/:id/show': '/:resource/:id'
// }))

server.use(router)

server.listen(4242, () => {
  // eslint-disable-next-line no-console
  console.log('json-server started on port 4242')
})
