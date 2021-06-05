<template>
  <div class="showPath">

    <navbar :activeIndex="3" :activeIndex2="3"></navbar>

    <div class="hotel">
        <span class="hotelname">{{hotelname+"到已选景点的路线："}}</span>
<!--        <span class="title">到已选景点的路线：</span>-->
    </div>

    <div class="haschosen">
      已选择景点：
      <el-tag
        v-for="sce in scenics"
        :key="sce"
        effect="plain"
        class="tags"
      >
        {{ sce }}
      </el-tag>
    </div>

    <el-divider class="devider"></el-divider>

    <div class="baidumap" v-loading="loading">
      <baidu-map
        class="map"
        :center="center"
        :zoom="15"
        :scroll-wheel-zoom="true"
      >
        <bm-scale anchor="BMAP_ANCHOR_CENTER"></bm-scale>
        <bm-marker
          :position="center"
          :dragging="true"
        >
          <bm-label
            :content="hotelname"
            :labelStyle="{ color: 'red', fontSize: '12px' }"
            :offset="{ width: -35, height: 30 }"
          />
        </bm-marker>
        <bm-marker
            v-for="pos in positions"
            :key="pos.index"
          :position="pos.lnglat"
          :dragging="true"
          animation="BMAP_ANIMATION_BOUNCE"
        >
          <bm-label
            :content="pos.position"
            :labelStyle="{ color: 'green', fontSize: '12px' }"
            :offset="{ width: -35, height: 30 }"
          />
        </bm-marker>
        <bm-polyline
          v-for="onepath in paths"
          :key="onepath.index"
          :path="onepath"
          stroke-color="blue"
          :stroke-opacity="0.5"
          :stroke-weight="6"
          @click="toPath(onepath)"
        ></bm-polyline>
      </baidu-map>
    </div>


  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
export default {
    components: {
    'navbar': NavBar,
  },
  data() {
    return {
        city:"",
        hotelname:"",
        scenics:[],
        oneScenic:false,
        firstScenic:"",
      loading:false,
      paths: [
        [
          { lng: 121.6292529148, lat: 31.2035397816 },
          { lng: 121.6282529148, lat: 31.2045397816 },
        ],
        [
          { lng: 121.6292529148, lat: 31.2035397816 },
          { lng: 121.6302529148, lat: 31.2035397816 },
        ],
      ],
      center: { lng: 121.6292529148, lat: 31.2035397816 },
      positions:[
        {position:"1",lnglat:{lng: 121.6282529148, lat: 31.2045397816}},
        {position:"2",lnglat:{lng: 121.6302529148, lat: 31.2035397816}},
      ]
    };
  },
  methods: {
    toPath(path) {
      var point1 = path[0];
      var point2 = path[1];
      // http://api.map.baidu.com/direction?origin=latlng:34.264642646862,108.95108518068|name:我家&destination=大雁塔&mode=driving&region=西安&output=html&src=webapp.baidu.openAPIdemo
      var url =
        "http://api.map.baidu.com/direction?origin=" +
        point1.lat +
        "," +
        point1.lng +
        "&destination=" +
        point2.lat +
        "," +
        point2.lng +
        "&mode=transit&region=" +
        encodeURIComponent(this.city) +
        "&output=html&src=webapp.baidu.openAPIdemo";
      window.open(url);
    },

    getInfos() {
      this.loading=true;
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/pathplan",
        params: {
          city: this.city,
          hotelname: this.hotelname,
          scenic:this.scenics,
        },
      })
        .then((res) => {
          // console.log(res.data.results); //在console中看到数据
          var array = res.data;
          this.loading=false;
          if (array == undefined || array.length <= 0) {
            console.log("no");
          } else {
            this.paths=array.paths;
            this.center=array.center;
            // this.positions=array.position;
            this.positions = array.position.map((item) => {
      return { position: item.position, lnglat: {lng:item.lng,lat:item.lat} };
    });
          }
        })
        .catch((res) => {
          alert("出错了！");
        });
      this.loading=false;
    },

    returnScenic() {
      this.$router.go(-1);
    },
    
  },

  mounted(){
    this.hotelname = this.$route.query.hotelname;
    this.city=this.$route.query.city;
    this.oneScenic=this.$route.query.oneScenic;
    this.firstScenic=this.$route.query.firstScenic;
    console.log(this.oneScenic);
    if(this.oneScenic=="true"){
      this.scenics.push(this.firstScenic);
      console.log("一个景点");
      console.log(this.scenics);
      console.log(this.oneScenic);
    }else{
      this.scenics = this.$route.query.scenics;
      console.log("多个景点");
      console.log(this.scenics);
    }
    this.getInfos();
  }
};
</script>

<style>
/* The container of BaiduMap must be set width & height. */
.hotel {
  margin-top: 15px;
  margin-left: 10%;
  width: 80%;
}
.hotelname {
    font-size: 30px;
    font-weight: bold;
    color: rgba(92, 200, 255, 1);
}
.title{
    font-size: 25px;
    color: #000;
}
.devider {
  color: #000;
  margin-top: 30px;
  margin-left: 5%;
  width: 90%;
}
.map {
  width: 100%;
  height: 100%;
}
.tags {
  margin-left: 3px;
}
.haschosen {
  text-align: left;
  font-size: 15px;
  font-weight: bord;
  /* background-color: rgb(255, 0, 0); */
  margin-top: 15px;
  margin-left: 7%;
  width: 86%;
  height: 20px;
}
.baidumap{
  margin-top: 30px;
  margin-left: 10%;
  width: 80%;
  height: 450px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
}
</style>
