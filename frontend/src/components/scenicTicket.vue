<template>
  <div class="scenicTicket" >
    <!-- <a :href="link"> -->
        <div class="item">
            <el-row>
                <div class="name" @click="jump()">{{ name }}</div>
              </el-row>
            <el-row>
                <div class="from">
                  <i class="el-icon-s-promotion"></i>
                  {{from}}
                  </div>
            </el-row>
            <el-row>
                <div class="type" v-if="hasType">
                  <el-tag size="mini" effect="dark">{{type}}</el-tag>
                </div>
            </el-row>
              <el-row>
                  <div class="typeandbuy">
                <span class="price">
                    {{"¥"+price.replace(/¥/g, '')}}
                  </span>
                  <span class="buy" v-if="hasBuy">
                      {{"已售:"+buy}}
                  </span>
                  </div>
            </el-row>
              <el-row>
                  <div class="tags">
                <span class="isReturnable" v-if="hasReturn">
                  <el-tag type="info" size="mini">{{isReturnable}}</el-tag>
                  </span>
                  <span class="bookTime" v-if="hasBook">
                  <el-tag type="info" size="mini">{{bookTime}}</el-tag>
                  </span>
                  <span class="bookTime" v-if="hasOut">
                  <el-tag type="info" size="mini">{{outTime}}</el-tag>
                  </span>
                  </div>
            </el-row>
            <el-row>
                  <div class="useTime" v-if="hasUse">{{useTime}}</div>
            </el-row>
            <el-row>
                  <div class="discription" v-if="hasDis" :style="discription_style">
                      <p class="dis" v-html="discription" ref="getheight"></p>
                      </div>
                      <div class="open" v-if="hasButton"><el-button type="text" @click="showAll">{{buttontext}}</el-button></div>
            </el-row>
            <el-row>
                <div class="placehold"></div>
            </el-row>
        </div>
    <!-- </a> -->
  </div>
</template>

<script>
export default {
  props: {
    name: {
      default: "暂无名称",
    },
    type: {
      default: "",
    },
    buy: {
      default: "",
    },
    from:{
      default:"",
    },
    isReturnable: {
      default: ""
    },
    bookTime:{
        default:""
    },
    outTime:{
        default:""
    },
    useTime:{
        default:""
    },
    discription:{
        default:""
    },
    price: {
      default: "暂无价格",
    },
    url: {
      default: "",
    },
  },
  data() {
    return {
        hasType:false,
        hasBuy:false,
        hasReturn:false,
        hasBook:false,
        hasOut:false,
        hasUse:false,
        hasDis:false,
        hasButton:false,
        showMore:true,
        buttontext:"展开",
      discription_style:"height:50px;overflow:hidden;margin-top: 8px;margin-left: 30px;margin-right: 30px;",
    };
  },
  methods: {
      jump() {
      window.open(this.url);
    },
    showAll(){
        if(this.showMore){
            this.discription_style="height:auto;margin-top: 8px;margin-left: 30px;margin-right: 30px;";
        this.showMore=false;
        this.buttontext="收起";
        }else{
            this.discription_style="height:50px;overflow:hidden;margin-top: 8px;margin-left: 30px;margin-right: 30px;";
        this.showMore=true;
        this.buttontext="展开";
        }
    },
    getHeight(){
      let height= this.$refs.getheight.offsetHeight;
      // if (height>50)
      console.log(height);
    }
  },
  mounted() {
      if(this.type!=""){
          this.hasType=true;
      }
      if(this.buy!=""){
          this.hasBuy=true;
      }
      if(this.isReturnable!=""){
          this.hasReturn=true;
      }
      if(this.bookTime!=""){
          this.hasBook=true;
      }
      if(this.outTime!=""){
          this.hasOut=true;
      }
      if(this.useTime!=""){
          this.hasUse=true;
      }
      if(this.discription!=""){
          this.hasDis=true;
          // console.log(this.discription.length)
      }
      
    this.$nextTick(()=>{ // 页面渲染完成后的回调
       let height = this.$refs.getheight.offsetHeight;
       if(height>=48){
         this.hasButton=true;
       }
    })
  },
};
</script>
<style scoped>
.item:hover {
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
}
.item {
    height: auto;
  width: 1000px;
  margin-top: 10px;
  justify-content: left;
  background: white;
  border: 1px solid #eee;
  transition: all 0.5s;
}
.name {
  margin-top: 15px;
  margin-left: 30px;
  margin-right: 30px;
  font-size: 20px;
  font-weight: bold;
  text-align: left;
  color: #212121;
}
.name:hover{
    color: rgb(0, 163, 245);
}
.type{
  margin-left: 30px;
  margin-right: 30px;
  margin-top: 8px;
  text-align: left;
}
.typeandbuy {
  margin-top: 8px;
  text-align: left;
  margin-left: 30px;
  margin-right: 30px;
}
.buy{
    font-size: 7px;
  font-weight: normal;
    text-align: left;
    margin-left: 5px;
  color: rgba(137, 161, 194, 0.815);;
}
.from {
  font-size: 12px;
  font-weight: normal;
  margin-top: 8px;
  text-align: left;
  color: rgba(63, 63, 63, 0.815);
  margin-left: 30px;
  margin-right: 30px;
}
.tags{
  margin-top: 8px;
  text-align: left;
  margin-left: 30px;
  margin-right: 30px;
}
.bookTime{
    margin-left: 5px;
}
.useTime{
  font-size: 12px;
  font-weight: normal;
  margin-top: 8px;
  text-align: left;
  color: rgba(19, 19, 19, 0.815);
  margin-left: 30px;
  margin-right: 30px;
}
.dis{
  font-size: 12px;
  font-weight: normal;
  text-align: left;
  color: rgba(63, 63, 63, 0.815);
  white-space: pre-line;
}
.open{
    margin-top: 3px;
    margin-bottom: 0px;
    text-align: left;
  margin-left: 30px;
  margin-right: 30px;
}
.price{
  font-size: 16px;
  font-weight: normal;
  text-align: left;
  color: rgba(37, 37, 37, 0.815);  
}
.placehold{
    height: 15px;
    margin-bottom: 0px;
}

</style>