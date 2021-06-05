<template>
  <div class="scenic">
    <el-popover
    placement="bottom"
    title="景点简介"
    width="350"
    trigger="hover"
    class="description"
    :content="description">
    <div class="lists" slot="reference" v-loading="loading">
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
              <el-col :offset="2">
                <div class="rank">
                  <el-tag effect="dark" size="mini">{{rank+"分"}}</el-tag>
                  </div>
              </el-col>
            </el-row>
            <el-row>
              <el-col :offset="2">
                <div class="address">
                  <i class="el-icon-location-outline"></i>
                  {{address}}
                  </div>
              </el-col>
            </el-row>
            <!-- <el-row>
              <el-col :offset="2">
                <div class="des">
                  <el-button size="mini" :type="buttontype" round @click="exchange" :plain="isClick">{{choose}}</el-button>
                </div>
              </el-col>
            </el-row> -->
          <!-- <el-row>
          <el-col :span="18" :offset="3">
            <div class="des">景点介绍</div>
          </el-col>
          </el-row>
          <el-row>
          <el-col :span="18" :offset="3">
            <div class="content">{{description}}</div>
          </el-col>
          </el-row> -->
        </div>
      </div>
    </div>
    </el-popover>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      default: "加载中……",
    },
    city: {
      default: "",
    },
    address:{
      default:"暂无地址",
    }
  },
  data() {
    return {
      loading:false,
      imgsrc: "",
      rank: "暂无评分",
      description: "加载中",
      shadow: "hover",
      isClick: false,
      choose:"点击选择",
      buttontype:"primary",
    };
  },
  methods: {
    exchange(){
      if(this.isClick){
        this.isClick = false;
        this.choose = "点击选择";
        this.buttontype = "primary";
      }else{
        this.isClick=true;
        this.choose="取消选择";
        this.buttontype="danger";
      }
    },
    getInfos() {
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/getSpotsInfo",
        params: {
          city: this.city,
          name: this.name,
        },
      })
        .then((res) => {
          // console.log(res.data.results); //在console中看到数据
          var array = res.data.data;
    this.loading=false;
          if (array == undefined || array.length <= 0) {
            console.log("no");
          } else {
            this.imgsrc = array.imgsrc;
            this.rank = array.rank;
            this.description = array.description;
          }
        })
        .catch((res) => {
          // alert("出错了！");
        });
    },
  },
  mounted() {
    this.loading=true;
    this.getInfos();
  },
};
</script>
<style scoped>
.lists {
  height: 180px;
  width: 1000px;
  display: flex;
  margin-top: 10px;
  justify-content: center;
  background-color: #fff;
}
.item {
  height: 180px;
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
  margin-left: 5%;
  margin-bottom: 10px;
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
  margin-top: 3%;
  width: 80%;
  justify-content: left;
}
.name {
  font-size: 30px;
  font-weight: bold;
  text-align: left;
  color: rgba(46, 45, 45, 0.815);
}
.rank {
  margin-top: 1%;
  text-align: left;
  color: rgba(46, 45, 45, 0.815);
}
.des {
  margin-top: 2%;
  text-align: left;
}
.address {
  margin-top: 1%;
  text-align: left;
  color: rgba(46, 45, 45, 0.815);
}
.selectitem {
  color: #333;
  display: flex;
  text-decoration: none;
  transition: all 0.5s;
  border: 2px solid blue;
}
.selectitem .item_pic {
  width: 20%;
  overflow: hidden;
}
</style>
