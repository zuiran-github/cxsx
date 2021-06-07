<template>
  <div class="hotel">
    <div class="lists">
      <div class="item" id="canchange">

        <div class="item_pic" fit="contain">
          <el-image :src="imgsrc" lazy class="img">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>

        <div class="item_content">
          <el-row>
            <el-col :offset="2">
              <div class="name">{{ name }}</div>
            </el-col>
          </el-row>
          <el-row>
            <el-col :offset="1">

              <div class="websites">
                <webs
                  v-for="web in webs"
                  :key="web.index"
                  :name="name"
                  :website="web.website"
                  :distance="web.distance"
                  :score="web.score"
                  :comments="web.comments"
                  :price="web.price"
                  :type="web.type"
                  :link="web.link"
                  :position="web.position"
                ></webs>
              </div>

              <el-button class="toRoad" 
      type="text" @click="toRoad"
      icon="el-icon-arrow-right">前往路线规划
              </el-button>

            </el-col>
          </el-row>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import web from "../components/newhw.vue";
export default {
  components: {
    "webs": web,
  },
  props: {
    name: {
      default: "暂无数据",
    },
    webs: {
      default: () => [
        {
          website: "暂无来源",
          score: 0.0,
          comments: 0,
          price: 0.0,
          type: "暂无类型",
          link: "",
          position:"",
        },
      ],
    },
    scenics:{
      default:[]
    },
    scenicandaddress:{
      default:[]
    },
    oneScenic:{
      default:true
    },
    firstScenic:{
      default:""
    },
    city:{
      default:""
    },
    imgsrc:{
      default:""
    },
  },
  data() {
    return {
      rank: "0",
      description: "加载中",
      shadow: "hover",
    };
  },
  methods: {
    toRoad(){
      let routeData=this.$router.resolve({
            path:'/hotel/hotelResult/path',

            //query/
            query: {
              scenics: this.scenics,
              scenicandaddress:this.scenicandaddress,
              hotelname: this.name,
              city: this.city,
              oneScenic:this.oneScenic,
              firstScenic:this.firstScenic,
            },
          });
          window.open(routeData.href);
    }
  },
  mounted() {
    // this.getInfos();
  },
};
</script>
<style scoped>
.lists {
  height: auto;
  width: 1100px;
  display: flex;
  margin-top: 10px;
  justify-content: center;
  background-color: #fff;
}
.item {
  height: auto;
  width: 100%;
  color: #333;
  display: flex;
  text-decoration: none;
  border: 1px solid #eee;
  transition: all 0.5s;
}
.item_pic {
  display: -webkit-box;

  -webkit-box-align: center;

  -webkit-box-pack: center;
  width: 200px;
  height: 200px;
  margin-left: 5%;
  margin-top: 15px;
  margin-bottom: 3%;
  overflow: hidden;
}
.img{
 transition: all 0.5s;
}
.img:hover{
  transform: scale(1.1);
}
.item:hover {
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
}
.item_content {
  height: 100%;
  width: 80%;
  justify-content: left;
}
.name {
  margin-top: 15px;
  font-size: 20px;
  font-weight: bold;
  text-align: left;
  color: #212121;
}
.websites {
  margin-top: 10px;
  text-align: left;
  margin-bottom: 10px;
}
.toRoad{
    margin-right: 10px;
    margin-bottom: 10px;
}
</style>
