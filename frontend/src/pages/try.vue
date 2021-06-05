<template>
  <section class="VideoBg">
    <video autoplay loop muted ref="video">
      <source src="../assets/videos/videobackground.mp4" type="video/mp4" />
    </video>
    <div class="VideoBg__content">
        <div class="slogen">让比价更便捷&nbsp;&nbsp;<br>&nbsp;&nbsp;让省钱更简单</div>
      <div class="round"></div>
        <!-- <div class="slogenshadow">让比价更便捷&nbsp;&nbsp;<br>&nbsp;&nbsp;让省钱更简单</div> -->
        <div class="title">百水千城</div>
        <el-button class="enter" icon="el-icon-s-promotion" round @click="enter">由此进入</el-button>
    </div>
  </section>
</template>


<script>
export default {
  data() {
    return {
      videoRatio: null,
      source: "../assets/videos/videobackground.mp4",
      img: "../assets/images/bg1.jpg",
    };
  },

  mounted() {
    this.setImageUrl();
    this.setContainerHeight();

    if (this.videoCanPlay()) {
      this.$refs.video.oncanplay = () => {
        if (!this.$refs.video) return;

        this.videoRatio =
          this.$refs.video.videoWidth / this.$refs.video.videoHeight;
        this.setVideoSize();
        this.$refs.video.style.visibility = "visible";
      };
    }

    window.addEventListener("resize", this.resize);
  },

  beforeDestroy() {
    window.removeEventListener("resize", this.resize);
  },

  methods: {
    resize() {
      this.setContainerHeight();

      if (this.videoCanPlay()) {
        this.setVideoSize();
      }
    },

    videoCanPlay() {
      return !!this.$refs.video.canPlayType;
    },

    setImageUrl() {
      if (this.img) {
        this.$el.style.backgroundImage = `url(${this.img})`;
      }
    },

    setContainerHeight() {
      this.$el.style.height = `${window.innerHeight}px`;
    },

    setVideoSize() {
      var width,
        height,
        containerRatio = this.$el.offsetWidth / this.$el.offsetHeight;

      if (containerRatio > this.videoRatio) {
        width = this.$el.offsetWidth;
      } else {
        height = this.$el.offsetHeight;
      }

      this.$refs.video.style.width = width ? `${width}px` : "auto";
      this.$refs.video.style.height = height ? `${height}px` : "auto";
    },
    enter() {
      this.$router.push("/ticket");
    }
  },
};
</script>


<style>
.VideoBg {
  position: relative;
  background-size: cover;
  background-position: center;
  overflow: hidden;
}

.VideoBg video {
  position: absolute;
  top: 50%;
  left: 50%;
  visibility: hidden;
  transform: translate(-50%, -50%);
}

.VideoBg__content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  text-align: center;
  background-color: rgba(63, 58, 58, 0.658);
}

.slogen {
  position: absolute;
  top:50%;
  left: 50%;
  transform:translate(-50%,-50%);
  font-family: "YuYangTi01";
  font-size: 60px;
  letter-spacing:5px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.788);
}

.title{
  position: absolute;
  top:2%;
  left: 2%;
  /* transform:translate(50%,50%); */
  font-family: "YuYangTi01";
  font-size: 30px;
  font-weight: bold;
  color: rgba(255,255,255,1);
}

.slogen:hover{
  box-shadow:  0 0 15px greenyellow;
}

/* .slogenshadow {
  position: absolute;
  top:50.5%;
  left: 51%;
  transform:translate(-50%,-50%);
  font-family: "YuYangTi01";
  font-size: 60px;
  letter-spacing:5px;
  font-weight: bold;
  color: rgba(66, 62, 62, 0.767);
} */

.round {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 35%;
  padding: 35% 0 0 0;
  border-radius: 50%;
  background-color: rgba(49, 47, 47, 0.459);
  transform: translate(-50%, -50%);
}

.round:hover{
 box-shadow:  0 0 15px rgb(37, 37, 37);
}

.enter{
  position: absolute;
  top: 50%;
  left: 67.5%;
  transform: translate(-20%, -50%);
}

</style>
