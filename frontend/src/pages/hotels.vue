<template>
  <div class="hotels">
    <scrBar></scrBar>
    <!-- <el-button type="primary" @click="onSubmitGet()">搜索</el-button> -->
    <el-col :span="20" :offset="1">
      <h1><span>{{" “"+params.departure+"”附近酒店的搜索结果：" }}</span></h1>
      <ul>
        <li class="list">
          <hotel
            v-for="intro in intros"
            :key="intro.name"
            :name="intro.name"
            :kind="intro.kind"
            :comments="intro.comments"
            :rate="intro.rate"
            :price="intro.price"
            :link="intro.link"
          ></hotel>
        </li>
      </ul>
    </el-col>
  </div>
</template>

<script>
import hotel from '../components/hotel.vue';
    import scrollBar from '../components/scrollBar.vue'
export default {
  components: {
    'hotel': hotel,
      'scrBar':scrollBar,
  },
  data() {
    return {
      intro: {
        name: "锦江之星那棵树的技术",
        kind: "经济型",
        comments: "",
        rate: 3.5,
        price: 0.0,
        link: "www.baidu.com",
      },
      intros: [],
      params: {
        departure: "上海市",
        destination: "",
        date1: "",
        date2: "",
        radio: 1,
        type: [],
      },
    };
  },
  methods: {
    onSubmitGet() {
      //   console.log(this.intro);
      //this.intro = [];
      this.$axios({
        method: "get",
        url: "api/tickets",
        param: {
          departure: this.params.departure,
          goDate: this.params.date1,
          backDate: this.params.date2,
        },
      })
        // .get("api/tickets")
        .then((res) => {
          //get()中的参数要与mock.js文件中的Mock.mock()配置的路由保持一致
          // axios.get('http://127.0.0.1:8000/users.json',).then(res => {//get()中的参数要与mock.js文件中的Mock.mock()配置的路由保持一致
          // console.log(res.data); //在console中看到数据
          //console.log(res.data.company);
          // this.intros = JSON.stringify(res.data)
          //   this.intro.company = JSON.stringify(res.data.data.company).replace(/\"/g, "");
          //   this.intro.flightID = JSON.stringify(res.data.data.flightID).replace(/\"/g, "");
          //   this.intro.dCityName = JSON.stringify(res.data.data.dCityName).replace(/\"/g, "");
          //   this.intro.aCityName = JSON.stringify(res.data.data.aCityName).replace(/\"/g, "");
          //   this.intro.dTime = JSON.stringify(res.data.data.dTime).replace(/\"/g, "");
          //   this.intro.aTime = JSON.stringify(res.data.data.aTime).replace(/\"/g, "");
          //   this.intro.cabin = JSON.stringify(res.data.data.cabin).replace(/\"/g, "");
          //   this.intro.price = JSON.stringify(res.data.data.price).replace(/\"/g, "");
          //   this.intro.link = JSON.stringify(res.data.data.tzurl).replace(/\"/g, "");
          // console.log(this.intros); //在console中看到数据
          this.intros = res.data.data;
          //  }
        })
        .catch((res) => {
          alert("出错了！");
        });
    },
  },
  mounted() {
    this.params.departure = this.$route.query.departure;
    this.params.date1 = this.$route.query.date1;
    this.params.date2 = this.$route.query.date2;
    console.log(this.params);
    this.onSubmitGet();
  },
};
</script>

<style scoped>
 .list {
   list-style-type:none;
   /* margin-top:50px; */
  /* line-height: 10px; */
   }
 .tickets{
   background-color:gray;
  /* line-height: 10px; */
  /* background-color: #658ea9 !important; */
 }
</style>