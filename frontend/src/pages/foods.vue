<template>
  <div class="foods">

    <navbar :activeIndex="3" :activeIndex2="3"></navbar>

    <div class="hotel">
        <span class="hotelname">{{city+"的特色美食："}}</span>
    </div>

    <el-button
      class="return"
      type="text"
      @click="returnScenic"
      icon="el-icon-arrow-left"
      >返回</el-button
    >

    <el-divider class="devider"></el-divider>

    <div class="searchResults" v-loading="loading">
      <ul
        class="list"
        v-show="hasFood"
      >
        <li
          v-for="food in foods"
          :key="food.index"
          class="list-item"
        >
          <food :name="food.name" :description="food.introduce[0]" :imgsrc="food.img[0]"> </food>
        </li>
      <h2 v-show="noFood">抱歉，好像没有搜到合适的结果……</h2>
      </ul>
    </div>


  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import food from "../components/food.vue";
export default {
    components: {
    'navbar': NavBar,
    "food":food,
  },
  data() {
    return {
        city:"",
        foods:[],
        loading:false,
        hasFood:false,
        noFood:false,
    };
  },
  methods: {

    getInfos() {
        this.loading=true;
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/getMeishiInfo",
        params: {
          city: this.city,
        },
      })
        .then((res) => {
          // console.log(res.data.results); //在console中看到数据
          var array = res.data.data;
          console.log(res);
    this.loading=false;
          if (array == undefined || array.length <= 0) {
            console.log("no");
            this.hasFood=false;
            this.noFood=true;
          } else {
            this.hasFood=true;
            this.noFood=false;
            this.foods=array;

          }
        })
        .catch((res) => {
          alert("出错了！");
        });
    },

    returnScenic() {
      this.$router.go(-1);
    },
    
  },

  mounted(){
    this.city=this.$route.query.city;
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
.list {
  list-style-type: none;
}
.searchResults{
  margin-top: 20px;
  margin-left: 10%;
  margin-bottom: 40px;
  width: 80%;
  height: 600px;
  /* background-color: rgb(43, 255, 0); */
  overflow: auto;
}
.return {
  position: absolute;
  top: 12%;
  left: 5%;
}
</style>
