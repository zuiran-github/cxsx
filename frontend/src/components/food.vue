<template>
  <div class="food">
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
                  <el-col :offset="2" :span="20">
                  <div class="discription" v-if="hasDis" :style="discription_style">
                      <p class="dis" v-html="description" ref="getheight"></p>
                      </div>
                      <div class="open" v-if="hasButton"><el-button type="text" @click="showAll">{{buttontext}}</el-button>
                      </div>
                      </el-col>
            </el-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      default: "椒盐虾虎",
    },
    description: {
      default: "当地人饭桌上的家常菜肴，它来自盛产虾虎的胶州湾，是一种汁鲜肉嫩、营养丰富的海鲜。常以椒盐的料理手法展现，其味道浓郁，香飘四溢，肥壮的脑部满是膏脂，入口鲜甜嫩滑。当地人饭桌上的家常菜肴，它来自盛产虾虎的胶州湾，是一种汁鲜肉嫩、营养丰富的海鲜。常以椒盐的料理手法展现，其味道浓郁，香飘四溢，肥壮的脑部满是膏脂，入口鲜甜嫩滑。当地人饭桌上的家常菜肴，它来自盛产虾虎的胶州湾，是一种汁鲜肉嫩、营养丰富的海鲜。常以椒盐的料理手法展现，其味道浓郁，香飘四溢，肥壮的脑部满是膏脂，入口鲜甜嫩滑。",
    },
    imgsrc:{
      default:"https://dimg05.c-ctrip.com/images/100r0k000000c3x0f8C40_R_510_300.jpg",
    }
  },
  data() {
    return {
        hasDis:false,
        hasButton:false,
        showMore:true,
        buttontext:"展开",
      discription_style:"height:80px;overflow:hidden;margin-top: 10px;",
    };
  },
  methods: {
      showAll(){
        if(this.showMore){
            this.discription_style="height:auto;margin-top: 10px;";
        this.showMore=false;
        this.buttontext="收起";
        }else{
            this.discription_style="height:80px;overflow:hidden;margin-top: 10px;";
        this.showMore=true;
        this.buttontext="展开";
        }
    },
    getHeight(){
      let height= this.$refs.getheight.offsetHeight;
      // if (height>50)
    //   console.log(height);
    },
  },
  mounted() {
      if(this.discription!=""){
          this.hasDis=true;
          // console.log(this.discription.length)
      }
      
    this.$nextTick(()=>{ // 页面渲染完成后的回调
       let height = this.$refs.getheight.offsetHeight;
       console.log(height);
       if(height>=64){
         this.hasButton=true;
       }
    })
  },
};
</script>
<style scoped>
.lists {
  height: auto;
  width: 1000px;
  display: flex;
  margin-top: 10px;
  justify-content: center;
  background-color: #fff;
}
.item {
  height: 100%;
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
  width: 160px;
  height: 160px;
  margin-left: 40px;
  margin-top: 10px;
  overflow: hidden;
}
.item_pic~.item_pic{
 margin-left: 15px;
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
  margin-top: 20px;
  width: 80%;
  justify-content: left;
}
.name {
  font-size: 25px;
  text-align: left;
  color: rgba(0, 0, 0, 0.815);
}
.dis{
  font-size: 15px;
  font-weight: normal;
  text-align: left;
  color: rgba(63, 63, 63, 0.815);
  white-space: pre-line;
}
.open{
    margin-bottom: 10px;
    text-align: left;
}
</style>
