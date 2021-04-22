<template>
  <div class="trainTicket">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>{{ trainID }}</span>
        <a v-bind:href="link">
          <el-button style="float: right; padding: 3px 0" type="text">去购票</el-button>
        </a>
      </div>
      <div class="text item">
        <el-col :span="18">
          <el-col :span="8">
            <el-row>{{dStation}}</el-row>
            <el-row>{{dtime}}</el-row>
          </el-col>
          <el-col :span="8">
            <el-row>————</el-row>
            <el-row>{{during}}</el-row>
          </el-col>
          <el-col :span="8">
            <el-row>{{aStation}}</el-row>
            <el-row>{{atime}}</el-row>
          </el-col>
        </el-col>
        <el-col>
          {{"¥" + price + "元起"}}
        </el-col>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      trainID: "",
      dStation:"",
      aStation:"",
      dtime:"",
      atime:"",
      during:"",
      link: "https://www.12306.cn/index/",
      price:0.00,

    };
  },
};
</script>

<style scoped>
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
</style>