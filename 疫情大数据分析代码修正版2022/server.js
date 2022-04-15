const express = require('express')
const app = express()
const port = 8012
app.use(express.static('dist'))
app.listen(port,()=>console.log(`服务器 ${port} 开启成功`))
