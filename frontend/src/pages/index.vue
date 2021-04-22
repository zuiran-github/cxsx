<template>
  <div class="index">
    <!-- <p class="homepage-hero-module">
          <p class="video-container">
              <p :style="fixStyle" class="filter"></p>
              <video :style="fixStyle" autoplay loop class="fillWidth" v-on:canplay="canplay">
                  <source src="../assets/videos/videobackground.mp4" type="video/mp4"/>
              </video>
              <p class="poster hidden" v-if="!vedioCanPlay">
                  <img :style="fixStyle" src="../assets/images/bg1.jpg" alt="">
              </p>
          </p>
      </p> -->
    <transition name="el-fade-in-linear">
      <div v-show="show">
        <!-- <h1 class="textbox2">百水千城</h1>
        <h1 class="textbox">百水千城</h1>
        <router-link to="/ticket"
          ><el-button class="button" type="text" @click="changebar()"
            >点此进入</el-button
          ></router-link
        > -->
        <h1 class="scroll">&nbsp; </h1>
        <h1 class="scroll">&nbsp; </h1>
        <h1 class="scroll">&nbsp; </h1>
        <scrBar></scrBar>
      </div>
    </transition>
  </div>
</template>

<script>
    import scrollBar from '../components/scrollBar.vue'
export default {
  name: "index",
  components:{
      'scrBar':scrollBar
    },
  data() {
    return {
      show: false,
      vedioCanPlay: false,
      fixStyle: "",
    };
  },
  methods: {
    showchange() {
      this.show = !this.show;
    },
    changebar() {
      NavBar.activeIndex = "1";
      NavBar.activeIndex2 = "1";
    },
    // canplay() {
    //   this.vedioCanPlay = true;
    // },
  },
  mounted() {
    this.showchange();
  },
  //   mounted: function () {
  //     window.onresize = () => {
  //       const windowWidth = document.body.clientWidth;

  //       const windowHeight = document.body.clientHeight;

  //       const windowAspectRatio = windowHeight / windowWidth;

  //       let videoWidth;

  //       let videoHeight;
  //       if (windowAspectRatio < 0.5625) {
  //         videoWidth = windowWidth;

  //         videoHeight = videoWidth * 0.5625;

  //         this.fixStyle = {
  //           height: windowWidth * 0.5625 + "px",

  //           width: windowWidth + "px",

  //           "margin-bottom": (windowHeight - videoHeight) / 2 + "px",

  //           "margin-left": "initial",
  //         };
  //       } else {
  //         videoHeight = windowHeight;

  //         videoWidth = videoHeight / 0.5625;

  //         this.fixStyle = {
  //           height: windowHeight + "px",

  //           width: windowHeight / 0.5625 + "px",

  //           "margin-left": (windowWidth - videoWidth) / 2 + "px",

  //           "margin-bottom": "initial",
  //         };
  //       }
  //     };

  //     window.onresize();
  //   },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* @import "../assets/fonts/font1.css" */
/* .homepage-hero-module,
.video-container {
  position: relative;
  height: 100vh;
  overflow: hidden;
}
.video-container .poster img,
.video-container video {
  z-index: 0;
  position: absolute;
}
.video-container .filter {
  z-index: 1;
  position: absolute;
  background: rgba(0, 0, 0, 0.4);
} */
#building {
  background: url("../assets/images/bg1.jpg");
  width: 100%;
  height: 100%;
  position: fixed;
  background-size: 100% 100%;
  /* z-index:-1;
	filter:blur(10px); 图层模糊*/
}
.textbox {
  height: 50%;
  font-family: "CuShuTi";
  color: rgba(252, 241, 249, 0.904);
  font-size: 120px;
  position: absolute;
  left: 50%;
  top: 25%;
  transform: translate(-50%, -50%);
}
.scroll {
  height: 25%;
  /* font-family: "CuShuTi";
  color: rgba(252, 241, 249, 0.904);
  font-size: 120px; */
  /* position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%); */
}
.textbox2 {
  font-family: "CuShuTi";
  color: rgba(0, 0, 0, 0.349);
  font-size: 120px;
  position: absolute;
  left: 51%;
  top: 26%;
  transform: translate(-50%, -50%);
}
.button {
  color: rgba(226, 226, 226, 0.829);
  font-family: "CuShuTi";
  font-size: 50px;
  position: absolute;
  left: 50%;
  top: 60%;
  transform: translate(-50%, -50%);
}
</style>