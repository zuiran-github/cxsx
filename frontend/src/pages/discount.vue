<template>
  <div class="discount">
    <transition name="el-fade-in-linear">
      <div id="building">
        <navbar :activeIndex="1" :activeIndex2="1"></navbar>
        <el-tabs type="border-card" class="searchBar">
  <el-tab-pane label="优惠搜索">
    <div class="citys">
    <el-col :span="9" :offset="2">
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
      <el-col :span="9" :offset="2">
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
    </div>
    <div class="others">
    <el-col :span="8" :offset="8">
        <el-input placeholder="请输入店铺名称" v-model="disname"></el-input>
    </el-col>
    </div>
    <div class="button">
      <el-col :span="8" :offset="8">
        <el-button @click="disSearch" type="primary">搜索优惠</el-button>
      </el-col>
    </div>
  </el-tab-pane>
  <el-tab-pane label="门票查询">
    
    <div class="citys">
    <el-col :span="9" :offset="2">
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
      <el-col :span="9" :offset="2">
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
    </div>
    <div class="others">
    <el-col :span="8" :offset="8">
        <el-input placeholder="请输入景点名称" v-model="scenicname"></el-input>
    </el-col>
    </div>
    <div class="button">
      <el-col :span="8" :offset="8">
        <el-button @click="scenicSearch" type="primary">搜索门票</el-button>
      </el-col>
    </div>
  </el-tab-pane>
  <el-tab-pane label="特色美食">
    <div class="citys">
    <el-col :span="9" :offset="2">
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
      <el-col :span="9" :offset="2">
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
    </div>
    <div class="button">
      <el-col :span="8" :offset="8">
        <el-button @click="foodSearch" type="primary">发现美食</el-button>
      </el-col>
    </div>
  </el-tab-pane>
</el-tabs>
      </div>
    </transition>
  </div>
</template>

<script>
    import scrollBar from '../components/scrollBar.vue'
    import NavBar from '../components/NavBar.vue'
export default {
  name: "ticketSearch",

  components:{
      'scrBar':scrollBar,
      'navbar':NavBar
    },

  methods: {

    disSearch() {
      if (this.city==undefined||this.city==""){
        alert("请选择城市！");
      }else{
        if(this.disname==undefined||this.disname==""){
          alert("请输入店铺名称！");
        }else{
          this.$router.push({
        name: "fooddiscount",

        //query/
        query: {
          disname: this.disname,
          city:this.city,
          province:this.province,
        },
      });
        }
      }
    },

    scenicSearch(){
      if (this.city==undefined||this.city==""){
        alert("请选择城市！");
      }else{
        if(this.scenicname==undefined||this.scenicname==""){
          alert("请输入景点名称！");
        }else{
          this.$router.push({
        name: "scenictickets",

        //query/
        query: {
          province: this.province,
          city:this.city,
          scenic:this.scenicname,
        },
      });
        }
      }
    },

    foodSearch(){
      if (this.city==undefined||this.city==""){
        alert("请选择城市！");
      }else{
        this.$router.push({
        name: "foods",

        //query/
        query: {
          city:this.city,
        },
      });
      }
    },

    showchange() {
      this.show = !this.show;
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
            alert("出错了！");
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
  },

  mounted() {
    this.provinces = this.states.map((item) => {
      return { value: `${item}`, label: `${item}` };
    });
    this.province="北京市";
    this.city="北京市";
  },

  data() {
    return {
      show: false,
      
      province: "",
      provinces: [],
      city: "",
      citys: [],
      
      nowcitys: [],
      hasCity: false,

      disname:"",
      scenicname:"",

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
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#building {
  background: url("../assets/images/bg22.jpg");
  width: 100%;
  height: 100%;
  position: fixed;
  background-size: 100% 100%;
}
.searchBar {
  position: absolute;
  left: 50%;
  top: 55%;
  width: 800px;
  height: 300px;
  transform: translate(-50%, -50%);
  background-color: rgb(221, 221, 221);
}
.citys{
  margin-top: 20px;
  height: 30px;
}
.others{
  text-align:center;
  margin-top: 30px;
  height: 30px;
}
.button{
  margin-top: 30px;
}
</style>
