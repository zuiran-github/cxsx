<template>
  <div class="fooddiscounts">
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
        <el-input placeholder="请输入优惠关键词" v-model="params.restaurant"></el-input>
      </el-col>
      <el-col :span="2" :offset="2">
        <el-button @click="findHotels" type="primary">搜索优惠</el-button>
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
      <ul class="list" v-if="hasdiscount">
        <li v-for="discount in discounts" :key="discount.index" class="list-item">
          <discount
            :name="discount.name"
            :description="discount.description"
            :link="discount.link"
            :nowprice="discount.nowprice"
            :pastprice="discount.pastprice"
            :count="discount.count"
          >
          </discount>
        </li>
      </ul>
      <h2 v-if="nodiscount">抱歉，好像没有相关优惠呢……</h2>
    </div>
  </div>
</template>

<script>
import fooddiscount from "../components/fooddiscount.vue";
import NavBar from "../components/NavBar.vue";
export default {
  components: {
    "discount": fooddiscount,
    "navbar": NavBar,
  },
  data() {
    return {
      discounts: [],
      loading: false,
      params: {
        restaurant: "",
      },
      hasCity:true,
      hasdiscount:false,
      nodiscount:false,
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
    };
  },
  methods: {
    onSubmitGet() {
      //   console.log(this.intro);
      //this.intro = [];

      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/getYouhuiInfo",
        params: {
          keyword: this.params.restaurant,
          city:this.city,
        },
      })
        // .get("api/tickets")
        .then((res) => {
          this.loading = false;
          var array = res.data.data;
          if (array == undefined || array.length <= 0) {
            this.hasdiscount = false;
            this.nodiscount=true;
          } else {
            this.hasdiscount = true;
            this.nodiscount=false;
            this.discounts = array;
          }
        })
        .catch((res) => {
          console.table(res);
          alert("出错了！！");
          //   this.hasHotel = false;
          // this.noHotel = true;
        });
    },

    findHotels() {
      if (this.params.restaurant == undefined||this.params.restaurant == "") {
        alert("请输入店铺名！");
      } else {
        if(this.city==undefined||this.city==""){
          alert("请选择城市！")
        }else{
          this.onSubmitGet();
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

    returnTo() {
      this.$router.go(-1);
    },
  },
  mounted() {
    this.loading = true;
    this.params.restaurant = this.$route.query.disname;
    this.province=this.$route.query.province;
    this.findCitys(this.province);
    this.city=this.$route.query.city;
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
