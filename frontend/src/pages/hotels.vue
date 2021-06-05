<template>
  <div class="hotels">
        <navbar :activeIndex="3" :activeIndex2="3"></navbar>
    <div class="searchbar">
      <!-- <el-col :span="3">
      </el-col> -->
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

    <el-button
      class="return"
      type="text"
      @click="returnScenic"
      icon="el-icon-arrow-left"
      >返回选择景点</el-button
    >

    <el-divider class="devider"></el-divider>

    <div class="haschosen">
      已选择景点：
      <span v-if="!oneScenic">
      <el-tag
        v-for="sce in params.scenics"
        :key="sce"
        effect="plain"
        class="tags"
      >
        {{ sce }}
      </el-tag>
      </span>
      <span v-if="oneScenic">
        <el-tag 
        effect="plain"
        class="tags">{{firstScenic}}</el-tag>
      </span>
    </div>

    <el-divider class="devider2"></el-divider>

    <div class="sort" v-if="oneScenic">
      <el-radio-group v-model="radio" @change="sort">
    <el-radio :label="1">综合</el-radio>
    <el-radio :label="2">价格升序</el-radio>
    <el-radio :label="3">价格降序</el-radio>
    <el-radio :label="4">距离升序</el-radio>
    <el-radio :label="5">评分降序</el-radio>
    <el-radio :label="6">评论数降序</el-radio>
  </el-radio-group>
    </div>

    <div class="searchResults" v-loading="loading">
      <ul
        class="list"
        v-if="hasHotel&!isMore"
      >
        <li
          v-for="hotel in hotels"
          :key="hotel.name"
          class="list-item"
        >
          <hotel :name="hotel.name" :webs="hotel.web" :scenics="params.scenics" :city="city" :imgsrc="hotel.picture" :oneScenic="oneScenic" :firstScenic="firstScenic"> </hotel>
        </li>
      </ul>
      <ul
        class="list"
        v-if="hasHotel&isMore"
      >
      <span class="notion">由于您选择的景点距离较远，因此为您推荐多组酒店。</span>
        <li
          v-for="(ahotel,index) in morehotels"
          :key="index"
          class="ahotels"
           @click="openlist(index)"
        >
          <div class="nsearchResult">
        <span class="resulttitle">{{"第"+(index+1)+"组搜索结果(点击以展开/收起)"}}</span>
            </div>
          <div class="results" v-if="nowopen==index">
          <hotel v-for="hotel in ahotel" :key="hotel.index" :name="hotel.name" :webs="hotel.web" :scenics="params.scenics" :city="city" :imgsrc="hotel.picture" :oneScenic="oneScenic" :firstScenic="firstScenic" class="hotel"> </hotel>
          <span class="notion">&nbsp;</span>
          </div>
        </li>
      </ul>
      <h2 v-if="noHotel">抱歉，好像没有搜到合适的结果……</h2>
    </div>
  </div>
</template>

<script>
import hotel from "../components/newht.vue";
import NavBar from "../components/NavBar.vue";
export default {
  components: {
    "hotel": hotel,
    'navbar': NavBar,
  },
  data() {
    return {
      hotels: [],
      morehotels:[],

      isMore:false,

      icon:"ei-icon-arrow-down",
      nowopen:0,

      value1: [],
      type:"",
      types:["全部","豪华型","高档型","舒适型","经济型","民宿"],

      radio:1,

      oneScenic:false,
      firstScenic:"",
      scenicandaddress:[],

      loading: false,
      params: {
        scenics: [],
        date1: "",
        date2: "",
      },
      city:"",
      province:"",
      count:0,
      hasHotel: false,
      noHotel:false,
      selectData: "",
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() < Date.now()||time.getTime()>Date.now()+10519200000;
        },
      },
    };
  },
  methods: {
    sort(value){
      this.loading=true;
      this.hotels=[];
      console.log("sort");
      var api = "http://127.0.0.1:8000/api/";
      switch(value){
        case 1:
          api=api+"jiudiansort";
          break;
        case 2:
          api=api+"priceascend";
          break;
        case 3:
          api=api+"pricedescend";
          break;
        case 4:
          api=api+"jiudiandistance";
          break;
        case 5:
          api=api+"jiudianscore";
          break;
        case 6:
          api=api+"jiudiancommends";
          break;
      }
      this.$axios({
        method: "get",
        url: api,
        params: {
          city:this.city,
          scenics: this.scenicandaddress,
          date1: this.params.date1,
          date2: this.params.date2,
          type:this.type,
        },
      })
        .then((res) => {
          this.loading=false;
          var array = res.data.data;
          if (array == undefined || array.length <= 0) {
            this.hasHotel = false;
            this.noHotel=true;
          } else {
            console.log(array);
            this.hasHotel = true;
            this.noHotel=false;
            this.hotels = array;
          }
        })
        .catch((res) => {
          console.table(res);
          alert("出错了！！");
        });
            this.$forceUpdate();

    },

    onSubmitGet() {
      //   console.log(this.intro);
      //this.intro = [];
      this.loading=true;
      this.hotels=[];
      this.radio=1;
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/jiudiansort",
        params: {
          city:this.city,
          scenics: this.scenicandaddress,
          date1: this.params.date1,
          date2: this.params.date2,
          type:this.type,
        },
      })
        // .get("api/tickets")
        .then((res) => {
          this.hotels=[];
          this.morehotels=[];
          this.loading=false;
          var type = res.data.type;
          var array = res.data.data;
          if (array == undefined || array.length <= 0) {
            this.hasHotel = false;
            this.noHotel=true;
          } else {
            console.log(array);
            this.hasHotel = true;
            this.noHotel=false;
            if(type==1){
            this.hotels = array;
            this.isMore=false;
            }
            if(type==0){
            this.isMore=true;
              for(var key in array){
                this.morehotels.push(array[key]);
              }
            }
            if(type==2){
              this.noHotel=true;
              this.hasHotel=false;
            }
          }
          console.log(this.scenicandaddress);
        })
        .catch((res) => {
          console.table(res);
          alert("出错了！！");
          console.log(this.scenicandaddress);
          //   this.hasHotel = false;
          // this.noHotel = true;
        });
    },

    findHotels() {
        if (!this.value1) {
          alert("请选择日期！");
        } else {
          this.params.date1=String(this.value1[0]);
          this.params.date2=String(this.value1[1]);
          this.onSubmitGet();
        }
    },

    openlist(index){
      if (this.nowopen==index){
        this.nowopen=-1;
      } else {
        this.nowopen=index;
      }
    },
    
    returnScenic() {
      this.$router.push({
            name: "hotelSearch",

            //query/
            query: {
              scenics: this.params.scenics,
              date1: String(this.value1[0]),
              date2: String(this.value1[1]),
              value1:this.value1,
              city: this.city,
              province:this.province,
              type:this.type,
              firstScenic:this.firstScenic,
              oneScenic:this.oneScenic,
              scenicandaddress:this.scenicandaddress,
            },
          });
    },
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
    this.params.date1 = this.$route.query.date1;
    this.params.date2 = this.$route.query.date2;
    this.oneScenic = this.$route.query.oneScenic;
    this.firstScenic = this.$route.query.firstScenic;
    this.scenicandaddress = this.$route.query.scenicandaddress;
    this.city=this.$route.query.city;
    this.province=this.$route.query.province;
    this.value1=[this.$route.query.date1,this.$route.query.date2];
    this.type=this.$route.query.type;
    if(this.oneScenic=="true"){
      this.params.scenics.push(this.firstScenic);
    }else{
    this.params.scenics = this.$route.query.scenics;
    }
    this.onSubmitGet();
  },
};
</script>

<style scoped>
.searchResults {
  margin-top: 20px;
  margin-left: 5%;
  width: 90%;
  height: 600px;
  /* background-color: rgba(191, 218, 217, 0.24); */
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
.devider2 {
  color: #000;
  margin-top: 18px;
  margin-left: 5%;
  width: 90%;
}
.haschosen {
  text-align: left;
  font-size: 15px;
  font-weight: bord;
  /* background-color: rgb(255, 0, 0); */
  margin-top: 15px;
  margin-left: 7%;
  width: 86%;
  height: auto;
}
.sort{
  margin-top: 15px;
  margin-left: 10%;
  width: 80%;
  height: 15px;
}
.ahotels{
  margin-top: 10px;
  background-color: rgba(159, 197, 255, 0.856);
  text-align: center;
  width: 100%;
}
.ahotels:hover{
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
}
.notion{
  font-size: 30px;
}
.nsearchResult{
  margin-top: 10px;
  height:auto;
  width:100%;
}
.resulttitle{
  margin-top: 5px;
  margin-bottom: 5px;
  font-size: 20px;
  color:black;
}
.resulttitle:hover{
  color: rgba(253, 231, 76, 1);;
}
.results {
  margin-top: 5px;
  height: 400px;
  overflow: auto;
}
/*.hotel{*/
/*  margin-left: 10px;*/
/*}*/
.list {
  list-style-type: none;
}
.tags {
  margin-left: 3px;
}
.selectitem {
  border: 1px solid rgba(137, 161, 194, 0.452);
}
.return {
  position: absolute;
  top: 12%;
  left: 5%;
}
</style>
