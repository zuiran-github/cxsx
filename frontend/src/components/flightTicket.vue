<template>
  <div class="flightTicket">
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
        <el-col :span="4">
          <span class="comp">{{ company + "-" + flightID }}</span>
        </el-col>
        <el-col :span="6">
          <span class="station">{{ dCityName + "——" + aCityName }}</span>
        </el-col>
        <el-col :span="9">
          <span class="time">{{ dTime.toLocaleString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '') + "——" + aTime.toLocaleString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '') }}</span>
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
      company: {
        default: '东方航空'
      },
      flightID: {
        default: '12345'
      },
      dCityName: {
        default: '始发地'
      },
      aCityName: {
        default: '目的地'
      },
      dTime: {
        default: '出发时间'
      },
      aTime: {
        default: '到达时间'
      },
      cabin: {
        default: '经济舱'
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