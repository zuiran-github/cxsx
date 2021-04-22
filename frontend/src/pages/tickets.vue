<template>
  <div class="tickets">
    <scrBar></scrBar>
    <!-- <el-button type="primary" @click="onSubmitGet()">搜索</el-button> -->
    <el-col :span="20" :offset="1">
      <h1><span>{{" “"+params.departure+"” 到 “"+params.destination+"”的搜索结果：" }}</span></h1>
      <ul>
        <li class="list">
          <flight
            v-for="intro in intros"
            :key="intro.flightID"
            :company="intro.company"
            :flightID="intro.flightID"
            :dCityName="intro.dCityName"
            :aCityName="intro.aCityName"
            :dTime="intro.dTime"
            :aTime="intro.aTime"
            :cabin="intro.cabin"
            :price="intro.price"
            :link="intro.tzurl"
          ></flight>
        </li>
      </ul>
    </el-col>
  </div>
</template>

<script>
import flightTicket from "../components/flightTicket.vue";
    import scrollBar from '../components/scrollBar.vue'
export default {
  components: {
    'flight': flightTicket,
      'scrBar':scrollBar,
  },
  data() {
    return {
      intr: {
        company: "",
        flightID: "",
        dCityName: "",
        aCityName: "",
        dTime: "",
        aTime: "",
        cabin: "经济舱",
        price: 0.0,
        link: "",
      },
      intros: [],
      params: {
        departure: "",
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
        url: "http://127.0.0.1:8000/api/allsearch",
        params: {
          departure: this.params.departure,
          destination: this.params.destination,
          goDate: this.params.date1,
          backDate: this.params.date2,
          trainOrPlane: this.params.radio,
          trainType: this.params.type,
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
    this.params.destination = this.$route.query.destination;
    this.params.date1 = this.$route.query.date1;
    this.params.date2 = this.$route.query.date2;
    this.params.radio = this.$route.query.radio;
    this.params.type = this.$route.query.type;
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
