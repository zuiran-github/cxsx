<template>
  <div class="hotelweb">
    <a :href="link">
      <el-card class="box-card" shadow="hover" @click.native="jump()">
        <div class="text item">
          <el-col :span="3">
            <span class="website">{{ website }}</span>
          </el-col>
          <el-col :span="3">
            <span class="distance">{{distance + "km" }}</span>
          </el-col>
          <el-col :span="3">
            <el-rate
              v-model="score"
              disabled
              show-score
              text-color="#ff9900"
              score-template="{value}"
            >
            </el-rate>
          </el-col>
          <el-col :span="3">
            <span class="comments">{{ "共" + comments + "条评论" }}</span>
          </el-col>
          <el-col :span="3">
            <span class="price">{{ "¥ " + price + "元起" }}</span>
          </el-col>
          <el-col :span="3">
            <span class="type">{{ type }}</span>
          </el-col>
        </div>
      </el-card>
    </a>
  </div>
</template>

<script>
export default {
  props: {
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
  },
  methods: {
    jump() {
      window.open(link);
    },
  },
  //   data:function() {
  //     return {
  //       company: "",
  //       flightID: "",
  //       dCityName: "",
  //       aCityName: "",
  //       dTime: "",
  //       aTime: "",
  //       cabin: "",
  //       price: 0.0,
  //       link: "",
  //     };
  //   },
};
</script>

<style scoped>
.flightTicket {
  margin-top: 10px;
}
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 100%;
}

.comp {
  /* font-size: 15px; */
  color: rgb(85, 85, 85);
  font-weight: bold;
}
.station {
  font-size: 18px;
  color: rgb(59, 59, 59);
  font-weight: bold;
}
.time {
  /* font-size: 12px; */
  color: rgba(255, 86, 86, 0.897);
  font-weight: bold;
}
.pri {
  font-size: 25px;
  color: rgb(45, 112, 255);
  font-weight: bold;
}
.list {
  list-style-type: none;
  /* margin-top:50px; */
  /* line-height: 10px; */
}
</style>