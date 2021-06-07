<template>
  <div class="web" >
    <!-- <a :href="link"> -->
        <div class="item" @click="jump()">
            <el-row>
                <div class="web">{{ website }}</div>
              </el-row>
              <el-row>
                <div class="type">
                  <el-tag size="mini" type="info">{{type}}</el-tag>
                  </div>
            </el-row>
              <el-row>
                <div class="score">
                  <el-tag effect="dark" size="mini" :type="rank">{{score+"分"}}</el-tag>
                  </div>
                  <div class="distance">
                      {{"共"+comments+"条评论"}}
                  </div>
            </el-row>
            <el-row>
                <div class="comments">
                  <i class="el-icon-location-outline"></i>
                  {{"距"+position+distance+"km"}}
                  </div>
            </el-row>
            <el-row>
                <div class="price">
                  {{"¥"+price}}
                </div>
            </el-row>
        </div>
    <!-- </a> -->
  </div>
</template>

<script>
export default {
  props: {
    name:{
      default:"",
    },
    website: {
      default: "暂无来源",
    },
    distance:{
      default:0.0,
    },
    score: {
      default: 0.0,
    },
    comments: {
      default: 0,
    },
    price: {
      default: 0.0,
    },
    type: {
      default: "暂无类型",
    },
    link: {
      default: "",
    },
    position:{
      default:"",
    }
  },
  data() {
    return {
      rank:"",
      shadow: "hover",
    };
  },
  methods: {
      jump() {
        this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/dianjifanhui",
        params: {
          hotelname:this.name,
          distance:this.distance,
          score:this.score,
          comments:this.comments,
          price:this.price,
        },
      })
        .then((res) => {
        })
        .catch((res) => {
          console.table(res);
          alert("出错了！！");
        });
      window.open(this.link);
    },
  },
  mounted() {
      if(this.score>=4.0){
          this.rank="success";
      }else{
          if(this.score>=3.0){
              this.rank="";
          }else{
              if(this.score>=2.0){
                  this.rank="warning";
              }else{
                  this.rank="info";
              }
          }
      }
  },
};
</script>
<style scoped>
.item:hover {
  border: 1px solid rgba(137, 161, 194, 0.452);
}
.item {
    float: left;
    height: auto;
  width: 100px;
  margin-left: 15px;
  justify-content: left;
  background: white;
  border: 1px solid #eee;
}
.web {
  font-size: 15px;
  font-weight: bold;
  text-align: left;
  margin-top: 7px;
  color: rgba(61, 61, 61, 0.808);
  /* color: rgba(64, 170, 223, 0.726); */
    margin-left: 3px;
}
.type {
  margin-top: 7px;
  text-align: left;
    margin-left: 3px;
}
.score {
  margin-top: 7px;
  text-align: left;
    margin-left: 8px;
}
.comments{
  font-size: 5px;
  font-weight: normal;
    margin-top: 7px;
    text-align: left;
  color: rgba(152, 177, 211, 0.815);
}
.distance {
  font-size: 12px;
  font-weight: normal;
  margin-top: 7px;
  text-align: left;
  color: rgba(63, 63, 63, 0.815);
    margin-left: 3px;
}
.price{
  font-size: 16px;
  font-weight: normal;
  margin-top: 7px;
  text-align: left;
  color: rgba(37, 37, 37, 0.815);  
    margin-left: 3px;
}

</style>
