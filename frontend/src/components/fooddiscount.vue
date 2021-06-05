<template>
  <div class="fooddiscount">
        <div class="item_content" @click="jump">
            <el-row>
              <el-col :offset="1">
                <div class="name">{{ name }}</div>
              </el-col>
            </el-row>
            <el-row>
                <el-col :offset="2" :span="20">
                <div class="address">
                  {{description}}
                  </div>
              </el-col>
            </el-row>
            <el-row>
                <el-col :offset="2">
                    <div class="count">{{count}}</div>
                </el-col>
            </el-row>
              <el-row>
              <el-col :offset="2">
                <div class="price"><font class="price">{{"¥"+nowprice}}</font><font class="pastprice">{{"¥"+pastprice}}</font>
                </div>
              </el-col>
            </el-row>
        </div>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      default: "加载中……",
    },
    description: {
      default: "暂无描述",
    },
    link:{
      default:"",
    },
    nowprice:{
        default:"0"
    },
    pastprice:{
        default:"0"
    },
    count:{
        default:"已售0"
    }
  },
  methods: {
      jump(){
        window.open(this.link);
      }
  },
  mounted() {
    this.loading=true;
  },
};
</script>
<style scoped>
.item_content:hover {
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
}
.item_content {
  width: 90%;
  margin-top: 10px;
  justify-content: center;
  background-color: #fff;
}
.name {
  font-size: 25px;
  font-weight: bold;
  margin-top: 15px;
  text-align: left;
  color: rgba(46, 45, 45, 0.815);
}
.address {
  margin-top: 7px;
  text-align: left;
  color: rgba(46, 45, 45, 0.815);
}
.count{
  font-size: 7px;
  font-weight: normal;
    margin-top: 10px;
    text-align: left;
    margin-left: 8px;
  color: rgba(137, 161, 194, 0.815);
}
.price{
    font-size: 30px;
    /* font-weight: bold; */
    color: rgb(66, 191, 253);
    text-align: left;
  margin-top: 10px;
  margin-bottom: 15px;
}
.pastprice{
  font-size: 7px;
  font-weight: normal;
    text-align: left;
    margin-left: 7px;
    text-decoration: line-through;
  color: rgba(137, 161, 194, 0.815);
}
</style>