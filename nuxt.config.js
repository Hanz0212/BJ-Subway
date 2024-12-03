module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: '北京地铁线路示意图',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '北京地铁线路示意图' }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/bj.ico' }]
  },
  css: ['~styles/cnuc/index.styl'],
  plugins: ['~plugins/element-ui'],

  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend(config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}
