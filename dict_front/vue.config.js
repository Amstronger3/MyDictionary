module.exports = {
  transpileDependencies: [
    'vuetify'
  ],

  devServer: {
    proxy: {
      '^/api': {
        target: '0.0.0.0:8000',
        changeOrigin: true
      },
    }
  }
}