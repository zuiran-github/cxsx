<template>
  <div class="hotel">
    <a :href="link">
      <el-card class="box-card" shadow="hover" @click.native="jump()">
      <!-- <div slot="header" class="clearfix">
        <span class="comp">{{ company + "-" + flightID }}</span>
        <a v-bind:href="link">
          <el-button style="float: right; padding: 3px 0" type="text"
            >去购票</el-button
          >
        </a>
      </div> -->
      <div class="text item">
        <!-- <el-col :span="18">
          <el-col :span="8">
            <el-row><span>{{ dCityName }}</span></el-row>
            <el-row><span>{{ dTime.toLocaleString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '') }}</span></el-row>
          </el-col>
          <el-col :span="8">
            <el-row>————</el-row>
            <el-row>{{ cabin }}</el-row>
          </el-col>
          <el-col :span="8">
            <el-row>{{ aCityName }}</el-row>
            <el-row>{{ aTime.toLocaleString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '') }}</el-row>
          </el-col>
        </el-col>
        <el-col :span="6">
          {{ "¥" + price + "元起" }}
        </el-col> -->
        <el-col :span="6">
          <span class="station">{{ name }}</span>
        </el-col>
        <el-col :span="3">
          <span class="comp">{{ kind }}</span>
        </el-col>
        <el-col :span="4">
          <span class="comp">{{ comments }}</span>
        </el-col>
        <el-col :span="6">
          <el-rate
  v-model="rate"
  disabled
  show-score
  text-color="#ff9900"
  score-template="{value}">
</el-rate>
        </el-col>
        <el-col :span="5">¥
          <span class="pri">{{price}}</span>元起
        </el-col>
      </div>
    </el-card>
    </a>
  </div>
</template>

<script>
export default {
    props: {
      name: {
        default: '锦江之星'
      },
      kind: {
        default: '经济型'
      },
      rate: {
        default: 3.6
      },
      comments: {
        default: '共1203条评论'
      },
      price: {
        default: 800
      },
      link: {
        default: '链接'
      }
    },
    methods:{
      jump(){
        window.open(link);
      }
    }
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
.flightTicket{
   margin-top:10px;
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

.comp{
  /* font-size: 15px; */
  color:rgb(85, 85, 85);
  font-weight:bold;
}
.station{
  font-size: 18px;
  color:rgb(59, 59, 59);
  font-weight:bold;
}
.time{
  /* font-size: 12px; */
  color:rgba(255, 86, 86, 0.897);
  font-weight:bold;
}
.pri{
  font-size: 25px;
  color:rgb(45, 112, 255);
  font-weight:bold;
}
</style>