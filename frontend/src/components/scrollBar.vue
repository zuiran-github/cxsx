<template>
  <el-carousel height="100" class="scrollBar" ref="carousel" @click.native="linkTo">
           <el-carousel-item class="lun_img" v-for="item in imgs" v-bind:key="item.url" >
             <img :src="item.url" style="height:100%;width:100%;"/>
           </el-carousel-item>
         </el-carousel>
</template>

<script>

export default {
    data(){
        return{
            imgs:[
                {url: require('../assets/images/bg4.jpg'), link: '/'},
        {url: require('../assets/images/bg1.jpg'), link: '/ticket'},
        {url: require('../assets/images/bg2.jpg'), link: '/hotel'},
        {url: require('../assets/images/bg5.jpg'), link: '/schedule'},
        {url: require('../assets/images/bg3.jpg'), link: '/discount'}
        ]
        }
    },
    methods: {
    linkTo () {
      let activeIndex = this.$refs.carousel.activeIndex
      this.$router.push({path:this.imgs[activeIndex].link})
    }
  }
}
</script>


<style>
  /* .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  } */
</style>