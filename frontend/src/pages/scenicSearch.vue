<template>
  <div class="scenicSearch">
    <navbar :activeIndex="3" :activeIndex2="3"></navbar>
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
            :key="item.value"
            :label="item.label"
            :value="item.value"
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
        <el-input placeholder="请输入景点名称(可选)" v-model="searchScenic"></el-input>
      </el-col>
      <el-col :span="2" :offset="2">
        <el-button @click="show" type="primary">搜索景点</el-button>
      </el-col>
    </div>
    
    <div class="searchHotel">
      <el-col :span="10" :offset="2">
        <el-date-picker
          v-model="value1"
          type="daterange"
          range-separator="至"
          start-placeholder="入住日期"
          end-placeholder="退房日期"
          value-format="yyyy-MM-dd"
          :picker-options="pickerOptions"
        >
        </el-date-picker>
      </el-col>
      <el-col :span="4" :offset="2">
        <el-select
          v-model="type"
          filterable
          reserve-keyword
          placeholder="请选择酒店类型"
        >
          <el-option
            v-for="item in types"
            :key="item"
            :label="item"
            :value="item"
          >
          </el-option>
        </el-select>
      </el-col>
      <el-col :span="2" :offset="2">
        <el-button @click="findHotels" type="primary">查询酒店</el-button>
      </el-col>
    </div>

    <el-divider class="devider"></el-divider>

    <div class="hotcitys"></div>

    <div class="haschosen">
      已选择景点(最多选择10个)：
      <el-tag
        v-for="sce in chooseScenics"
        :key="sce.index"
        effect="plain"
        class="tags"
        closable
        @close="deleteScenic(sce)"
      >
        {{ sce }}
      </el-tag>
    </div>

    <div class="searchResults" v-loading="listloading">
      <ul
        class="list"
        v-infinite-scroll="load"
        infinite-scroll-disabled="disabled"
        infinite-scroll-immediate="false"
        v-show="hasScenics"
      >
        <li
          v-for="scenic in scenics"
          :key="scenic.index"
          class="list-item"
          v-on:click="choose(scenic)"
        >
          <scenic
            class="secnic"
            :name="scenic.name"
            :city="city"
            :address="scenic.address"
          ></scenic>
        </li>
      </ul>
      <h2 v-show="noScenic">抱歉，好像没有搜到合适的结果……</h2>
      <p v-if="loading">加载中...</p>
      <p v-if="noMore">没有更多了</p>
    </div>

  </div>
</template>

<script>
import scenic from "../components/scenic.vue";
import NavBar from "../components/NavBar.vue";
export default {
  components: {
    "navbar": NavBar,
    "scenic": scenic,
  },
  data() {
    return {
      value1: "",
      date1: "",
      date2: "",
      types:["全部","豪华型","高档型","舒适型","经济型","民宿"],
      type:"全部",

      province: "",
      provinces: [],
      city: "",
      citys: [],
      searchScenic:"",

      truecity:"",
      trueprovince:"",

      nowcitys: [],
      hasCity: false,
      count: 1,

      scenics: [],
      chooseScenics: [],
      scenicandaddress:[],

      hasScenic: false,
      hasScenics:false,
      noScenic: false,

      oneScenic:"",
      sceniccounts:0,

      loading: false,
      noMore: false,

      listloading: false,
      timedisable: true,
      states: [
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
      pickerOptions: {
        disabledDate(time) {
          return (
            time.getTime() < Date.now() ||
            time.getTime() > Date.now() + 10519200000
          );
        },
      },
    };
  },

  computed: {
    nomore() {
      return this.noMore;
    },
    disabled() {
      return this.loading || this.nomore;
    },
  },

  mounted() {
    this.provinces = this.states.map((item) => {
      return { value: `${item}`, label: `${item}` };
    });
    this.province = "北京市";
    this.hasScenic = false;
    if (this.$route.query.date1){
      this.date1=this.$route.query.date1;
    }
    if (this.$route.query.date2){
      this.date2=this.$route.query.date2;
    }
    if (this.$route.query.province){
      this.province=this.$route.query.province;
      this.trueprovince=this.$route.query.province;
    }
    this.findCitys(this.province);
    if (this.$route.query.city){
      this.truecity=this.$route.query.city;
      this.city=this.$route.query.city;
    }
    this.show();
    if (this.$route.query.type){
      this.type=this.$route.query.type;
    }
    if (this.$route.query.value1){
      this.value1=this.$route.query.value1;
    }
    if (this.$route.query.firstScenic){
      this.scenicandaddress=this.$route.query.scenicandaddress;
      let ons = this.$route.query.oneScenic;
      if(ons){
        this.chooseScenics.push(this.$route.query.firstScenic);
        console.log(this.chooseScenics)
        // this.$forceUpdate();
      }
      else{
        if(this.$route.query.scenics){
          this.chooseScenics=this.$route.query.scenics;
        }
      }

    }
  },

  methods: {
    show() {
      if (this.province == "") {
        alert("请选择省份！");
      } else {
        if (this.city == "") {
            alert("请选择城市！");
        } else {
          this.count=1;
          if(this.searchScenic==undefined||this.searchScenic==""){
            if(this.province!=this.trueprovince){
              this.hasScenic = false;
              this.chooseScenics = [];
              this.scenicandaddress = [];
            }
            this.listloading = true;
          var url =
            "http://api.map.baidu.com/place/v2/search?query=" +
            encodeURIComponent("旅游景点") +
            "&region=" +
            encodeURIComponent(this.city) +
            "&output=json&page_size=4&page_num=0&ak=umawrZEEKAx20cCK1NHsRLmLYwmgpURB"+"&callback=showScenic";
          // this.$axios({
          //   method: "get",
          //   url: url,
          // })
          this.$jsonp(url)
            .then((res) => {
                this.showScenic(res);
            })
            .catch((res) => {
              alert("出错了！");
            });
          }else{
            if(this.province!=this.trueprovince){
              this.hasScenic = false;
              this.chooseScenics = [];
              this.scenicandaddress = [];
            }
            this.listloading = true;
          var url =
            "http://api.map.baidu.com/place/v2/search?query=" +
            encodeURIComponent(this.searchScenic) +"&tag="+
            encodeURIComponent("旅游景点")+ "&region=" +
            encodeURIComponent(this.city) +
            "&output=json&page_size=4&page_num=0&ak=umawrZEEKAx20cCK1NHsRLmLYwmgpURB"+"&callback=showScenic";
          // this.$axios({
          //   method: "get",
          //   url: url,
          // })
          this.$jsonp(url)
            .then((res) => {
                this.showScenic(res);
            })
            .catch((res) => {
              alert("出错了！");
            });
          }
        }
      }
      this.trueprovince=this.province;
      this.truecity=this.city;
      this.listloading=false;
    },

    showScenic(res){
      var array = res.results;
                this.listloading = false;
                if (array == undefined || array.length <= 0) {
                  console.log("no");
                  this.hasScenics = false;
                  this.noScenic = true;
                } else {
                  this.scenics = [];
                  this.$forceUpdate();
                  this.hasScenics = true;
                  this.noScenic = false;
                  array.forEach((item, index, array) => {
                    this.scenics.push({
                      name: item.name,
                      address: item.address,
                    });
                  });
                  this.timedisable = false;
                  this.$forceUpdate();
                }
    },

    load() {
      this.loading = true;
      if (this.province == "") {
        alert("请选择省份！");
      } else {
        if (this.city == "") {
          if (
            this.province == "北京市" ||
            this.province == "天津市" ||
            this.province == "上海市" ||
            this.province == "重庆市"
          ) {
            var url =
              "http://api.map.baidu.com/place/v2/search?query=" +
              encodeURIComponent("旅游景点") +
              "&region=" +
              encodeURIComponent(this.province) +
              "&output=json&page_size=4&page_num=" +
              this.count +
              "&ak=umawrZEEKAx20cCK1NHsRLmLYwmgpURB"+"&callback=loadScenic";
              this.$jsonp(url)
            .then((res)=>{
                this.loadScenic(res);
            })
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
            //       this.noMore = true;
            //     } else {
            //       array.forEach((item, index, array) => {
            //         this.scenics.push({
            //           name: item.name,
            //           address: item.address,
            //         });
            //       });
            //       this.count = this.count + 1;
            //     }
            //   })
            //   .catch((res) => {
            //     alert("出错了！");
            //   });
          } else {
            alert("请选择城市！");
          }
        } else {
          if(this.searchScenic==undefined||this.searchScenic==""){
            this.loading = true;
          var url =
            "http://api.map.baidu.com/place/v2/search?query=" +
            encodeURIComponent("旅游景点") +
            "&region=" +
            encodeURIComponent(this.city) +
            "&output=json&page_size=4&page_num=" +
            this.count +
            "&ak=umawrZEEKAx20cCK1NHsRLmLYwmgpURB"+"&callback=loadScenic";
          }
          else{
            this.listloading = true;
          this.chooseScenics = [];
          var url =
            "http://api.map.baidu.com/place/v2/search?query=" +
            encodeURIComponent(this.searchScenic) +"&tag="+
            encodeURIComponent("旅游景点")+ "&region=" +
            encodeURIComponent(this.city) +
            "&output=json&page_size=4&page_num=" +
            this.count +
            "&ak=umawrZEEKAx20cCK1NHsRLmLYwmgpURB"+"&callback=loadScenic";
          }

          this.$jsonp(url)
            .then((res) => {
              this.loadScenic(res);
            })
            .catch((res) => {
              alert("加载出错了！");
            });
        }
      }
      this.listloading = false;
    },

    loadScenic(res){
      this.loading=false;
                var array = res.results;
                if (array == undefined || array.length <= 0) {
                  console.log("no");
                  this.noMore = true;
                } else {
                  array.forEach((item, index, array) => {
                    this.scenics.push({
                      name: item.name,
                      address: item.address,
                    });
                  });
                  this.count = this.count + 1;
                }
    },

    deleteScenic(name){
      var index=this.chooseScenics.indexOf(name)
      this.chooseScenics.splice(index,1);
      this.scenicandaddress.splice(index,1);
      if (this.chooseScenics.length <= 0) {
        this.hasScenic = false;
      }
    },

    choose(item) {
      if (this.chooseScenics == []) {
        this.chooseScenics.push(item.name);
        this.scenicandaddress.push(item.name+" "+item.address)
        console.log("push");
        this.hasScenic = true;
      } else {
        if (this.chooseScenics.indexOf(item.name) > -1) {
          this.deleteScenic(item.name);
          console.log("delete");
          if (this.chooseScenics.length <= 0) {
            this.hasScenic = false;
          }
        } else {
          if (this.chooseScenics.length >= 10) {
            alert("选择景点数量超过10个！");
          } else {
            this.chooseScenics.push(item.name);
            this.scenicandaddress.push(item.name+" "+item.address)
            console.log("push");
          }
        }
      }
      // this.$forceUpdate();
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
        // this.$axios({
        //   method: "get",
        //   url: url,
        // })
        this.$jsonp(url)
          .then((res) => {
            // console.log(res.data.results); //在console中看到数据
            // this.loading = false;
            // var array = res.data.results;
            // if (array == undefined || array.length <= 0) {
            //   console.log("no");
            // } else {
            //   array.forEach((item, index, array) => {
            //     this.citys.push(item.name);
            //     this.$forceUpdate();
            //   });
            // }
             this.getCitys(res);
          })
          .catch((res) => {
            alert("百度出错了！");
          });
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
            }
    },

    findHotels() {
      if (this.chooseScenics.length <= 0) {
        alert("请选择至少一个景点！");
      } else {
        if (this.value1 == "") {
          alert("请选择日期！");
        } else {
          var onescenic = false;
          if(this.chooseScenics.length==1){
            onescenic = true;
          }
          this.$router.push({
            name: "hotels",

            //query/
            query: {
              scenics: this.chooseScenics,
              scenicandaddress:this.scenicandaddress,
              date1: String(this.value1[0]),
              date2: String(this.value1[1]),
              city: this.truecity,
              province:this.trueprovince,
              type:this.type,
              firstScenic:this.chooseScenics[0],
              oneScenic:onescenic,
            },
          });
        }
      }
    },
  },
};
</script>
<style scoped>
.searchResults {
  margin-top: 20px;
  margin-left: 10%;
  margin-bottom: 40px;
  width: 80%;
  height: 600px;
  /* background-color: rgb(43, 255, 0); */
  overflow: auto;
}
.searchbar {
  margin-top: 15px;
  margin-left: 10%;
  width: 80%;
  height: 25px;
}
.devider {
  color: #000;
  margin-top: 38px;
  margin-left: 5%;
  width: 90%;
}
.haschosen {
  text-align: left;
  font-size: 15px;
  font-weight: bord;
  /* background-color: rgb(255, 0, 0); */
  margin-top: 18px;
  margin-left: 7%;
  width: 86%;
  height: auto;
}
.list {
  list-style-type: none;
}
.tags {
  margin-left: 3px;
}
.searchHotel {
  margin-top: 30px;
  margin-left: 10%;
  width: 80%;
  height: 25px;
}
.selectScenic {
  border: 2px solid blue;
}
</style>
