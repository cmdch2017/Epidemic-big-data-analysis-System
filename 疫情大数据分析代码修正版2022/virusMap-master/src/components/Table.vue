<template>

  <div class="home">
    <h2>预测分析</h2>
    <div class="slider">

      <el-carousel :interval="5000" arrow="always" :height="banH +'px'">

        <el-carousel-item v-for="img in banImgList" :key="img.id">

          <img :src="img.image" class="picImg" />

        </el-carousel-item>

      </el-carousel>

    </div>

  </div>

</template>
<script>
export default {

  data () {

    return {

      banH: 0,

      banImgList: [
        { id: 0, image: require('../assets/image/python.jpg') },

        { id: 1, image: require('../assets/image/CA1.jpg') },
        { id: 2, image: require('../assets/image/CA2.jpg') },

        { id: 3, image: require('../assets/image/CA3.jpg') },
        { id: 4, image: require('../assets/image/CA4.jpg') },


        { id: 5, image: require('../assets/image/WA1.jpg') },

        { id: 6, image: require('../assets/image/WA2.jpg') },
        { id: 7, image: require('../assets/image/WA3.jpg') },
        { id: 8, image: require('../assets/image/WA4.jpg') },
        { id: 9, image: require('../assets/image/WA5.jpg') },

        { id: 10, image: require('../assets/image/C1.jpg') },

        { id: 11, image: require('../assets/image/C2.jpg') },

        { id: 12, image: require('../assets/image/C3.jpg') },
        { id: 13, image: require('../assets/image/C4.jpg') },
        { id: 14, image: require('../assets/image/C5.jpg') },
        { id: 15, image: require('../assets/image/America1.jpg') },
        { id: 16, image: require('../assets/image/America2.jpg') },





      ],

    }

  },

  methods: {

    setbanH () {

      this.banH = 700

    }

  },

  mounted () {

    this.setbanH()

    window.addEventListener('resize', () => {

      this.setbanH()

    }, false)

  },

}

</script>