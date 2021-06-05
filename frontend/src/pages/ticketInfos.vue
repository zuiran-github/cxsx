<template>
  <div class="ticketinfos">
    <navbar :activeIndex="4" :activeIndex2="4"></navbar>
    <div class="searchbar">
      <el-col :span="4" :offset="2">
        <el-select
          v-model="province"
          filterable
          reserve-keyword
          placeholder="请选择省份"
          @change="findCitys"
        >
          <el-option
            v-for="item in provinces"
            :key="item"
            :label="item"
            :value="item"
          >
          </el-option>
        </el-select>
      </el-col>
      <el-col :span="4" :offset="2">
        <el-select
          v-model="city"
          filterable
          :disabled="!hasCity"
          placeholder="请选择城市"
        >
          <el-option
            v-for="item in citys"
            :key="item"
            :label="item"
            :value="item"
          >
          </el-option>
        </el-select>
      </el-col>
      <el-col :span="4" :offset="2">
        <el-input placeholder="请输入景点名称" v-model="params.scenic"></el-input>
      </el-col>
      <el-col :span="2" :offset="2">
        <el-button @click="findScenics" type="primary">搜索门票</el-button>
      </el-col>
    </div>

    <el-button
      class="return"
      type="text"
      @click="returnTo"
      icon="el-icon-arrow-left"
      >返回</el-button
    >

    <el-divider class="devider"></el-divider>

    <div class="hotcitys"></div>

    <div class="searchResults" v-loading="loading">
      <ul class="list"
      v-infinite-scroll="load"
        infinite-scroll-disabled="disabled"
        infinite-scroll-immediate="false"
        v-if="hasTicket"
        >
        <li v-for="i in count" :key="i" class="list-item">
          <scenicTicket
            :name="tickets[i].name"
            :discription="tickets[i].discription"
            :url="tickets[i].url"
            :type="tickets[i].type"
            :buy="tickets[i].buy"
            :from="tickets[i].from"
            :isReturnable="tickets[i].isReturnable"
            :bookTime="tickets[i].bookTime"
            :outTime="tickets[i].outTime"
            :useTime="tickets[i].useTime"
            :price="tickets[i].price"
          >
          </scenicTicket>
        </li>
      </ul>
      <p v-if="loadmore">加载中...</p>
      <p v-if="nomore">没有更多了</p>
      <h2 v-if="noTicket">抱歉，好像没有相关景点呢……</h2>
    </div>
  </div>
</template>

<script>
import scenicTicket from "../components/scenicTicket.vue";
import NavBar from "../components/NavBar.vue";
export default {
  components: {
    "scenicTicket": scenicTicket,
    "navbar": NavBar,
  },
  data() {
    return {
        provinces: [
        "北京市",
        "天津市",
        "上海市",
        "重庆市",
        "河北省",
        "山西省",
        "辽宁省",
        "吉林省",
        "黑龙江省",
        "江苏省",
        "浙江省",
        "安徽省",
        "福建省",
        "江西省",
        "山东省",
        "河南省",
        "湖北省",
        "湖南省",
        "广东省",
        "海南省",
        "四川省",
        "贵州省",
        "云南省",
        "陕西省",
        "甘肃省",
        "青海省",
        "内蒙古自治区",
        "广西壮族自治区",
        "西藏自治区",
        "宁夏回族自治区",
        "新疆维吾尔自治区",
      ],
      province:"",
      citys:[],
      city:"",
      tickets: [],
      alltickets:0,
      hasCity:false,
      hasTicket:false,
      noTicket:false,
      count:10,
      loading: false,
      params: {
        scenic: "",
      },
      loadmore:false,
    };
  },

  computed: {
    nomore() {
      return this.count>this.alltickets;
    },
    disabled() {
      return this.loadmore || this.nomore;
    },
  },

  methods: {
    onSubmitGet() {
      //   console.log(this.intro);
      //this.intro = [];
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/getTicketInfo",
        params: {
          keyword: this.params.scenic,
          city:this.city,
        },
      })
        // .get("api/tickets")
        .then((res) => {
          this.loading = false;
          var array = res.data.data;
        //   console.log(array);
          if (array == undefined || array.length <= 0) {
            this.hasTicket = false;
            this.noTicket = true;
          } else {
            this.hasTicket = true;
            this.noTicket = false;
            var infos = [];
            for(var key in array){
                var array1 = array[key];
                for (var key1 in array1){
                    var array2 = array1[key1];
                    for (var key2 in array2){
                        var list = array2[key2];
                        infos.push.apply(infos,list);
                        
            // console.log(list);
                    }
                }
            }
            this.tickets=infos;
            this.alltickets=infos.length;
          }
        })
        .catch((res) => {
          console.table(res);
          alert("出错了！！");
          //   this.hasHotel = false;
          // this.noHotel = true;
        });
    },

    findScenics() {
      if (this.params.scenic == ""||this.params.scenic == undefined) {
        alert("请输入景点名称！");
      } 
      else {
        if (this.city=="" || this.city==undefined){
            alert("请选择城市！");
        }
        else{
          this.$router.push({
            name: "scenicticket",

            //query/
            query: {
              scenic: this.params.scenic,
              city: this.city,
              province:this.province,
            },
          });
          
        }
      }
    },

    findCitys(prov) {
      this.city = "";
      this.citys = [];
      if (
        prov == "北京市" ||
        prov == "天津市" ||
        prov == "上海市" ||
        prov == "重庆市"
      ) {
        this.hasCity = false;
        this.city = prov;
      } else {
        this.hasCity = true;
        var url =
          "http://api.map.baidu.com/place/v2/search?query=" +
          encodeURIComponent("商圈") +
          "&region=" +
          encodeURIComponent(prov) +
          "&output=json&page_size=20&ak=umawrZEEKAx20cCK1NHsRLmLYwmgpURB"+"&callback=getCitys";

            this.$jsonp(url)
            .then((res)=>{
                console.log(res);
                this.getCitys(res);
            }).catch((res) => {
            alert("出错了！");
          });

        // this.$axios({
        //   method: "get",
        //   url: url,
        // })
        //   .then((res) => {
        //     // console.log(res.data.results); //在console中看到数据
        //     this.loading = false;
        //     var array = res.data.results;
        //     if (array == undefined || array.length <= 0) {
        //       console.log("no");
        //     } else {
        //       array.forEach((item, index, array) => {
        //         this.citys.push(item.name);
        //         this.$forceUpdate();
        //       });
        //     }
        //   })
        //   .catch((res) => {
        //     alert("出错了！");
        //   });
      }
    },

    getCitys(res){
        this.loading = false;
            var array = res.results;
            if (array == undefined || array.length <= 0) {
              console.log("no");
            } else {
              array.forEach((item, index, array) => {
                this.citys.push(item.name);
                this.$forceUpdate();
              });
                  console.log("good!")
            }
    },

    load(){
        this.loadmore=true;
        this.count+=6;
        this.loadmore=false;
    },

    returnTo() {
      this.$router.go(-1);
    },


  },
  mounted() {
    this.loading = true;
    this.province = this.$route.query.province;
    this.params.scenic=this.$route.query.scenic;
    this.findCitys(this.province);
    this.city = this.$route.query.city;
    // console.log(this.params);
    this.onSubmitGet();
  },
};
</script>

<style scoped>
.searchResults {
  margin-top: 25px;
  margin-left: 10%;
  margin-bottom: 30px;
  width: 80%;
  height: 800px;
  text-align: center;
  /* background-color: rgba(191, 218, 217, 0.24); */
  overflow: auto;
}
/* .searchResults::-webkit-scrollbar {
        display: none;
    } */
.searchbar {
  margin-top: 15px;
  margin-left: 10%;
  width: 80%;
}
.devider {
  color: #000;
  margin-top: 70px;
  margin-left: 5%;
  width: 90%;
}
.list {
  list-style-type: none;
}
.return {
  position: absolute;
  top: 82px;
  left: 5%;
}
</style>
