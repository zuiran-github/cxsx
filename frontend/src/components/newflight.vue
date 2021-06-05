<template>
  <div class="newflight">
    <div class="lists" @click="jump()">
      <el-col>
        <div class="flight">{{ flightID }}</div>
        <div class="company"><el-tag effect="dark" size="mini">{{company}}</el-tag></div>
      </el-col>
      <el-col>
        <div class="dTime">
          {{dTime.toLocaleString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '')}}
        </div>
        <div class="dCity">{{dCityName}}</div>
      </el-col>
      <el-col>
        <div class="divid">————
        </div>
        <div class="cabin">{{cabin}}</div>
      </el-col>
      <el-col>
        <div class="aTime">
          {{aTime.toLocaleString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '')}}
        </div>
        <div class="aCity">{{aCityName}}</div>
      </el-col>
      <el-col>
          <div class="price">{{"¥"+price}}</div>
      </el-col>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    company: {
      default: "东方航空",
    },
    flightID: {
      default: "12345",
    },
    dCityName: {
      default: "始发地",
    },
    aCityName: {
      default: "目的地",
    },
    dTime: {
      default: "2021-06-24 07:15",
    },
    aTime: {
      default: "2021-06-24 07:15",
    },
    cabin: {
      default: "经济舱",
    },
    price: {
      default: 800,
    },
    link: {
      default: "",
    },
  },
  methods: {
      jump(){
        window.open(this.link);
      }
  },
};
</script>
<style scoped>
.lists {
  height: 100px;
  width: 550px;
  display: flex;
  margin-top: 12px;
  justify-content: center;
  background-color: rgb(255, 255, 255);
  text-decoration: none;
  border: 1px solid #eee;
  transition: all 0.5s;
}
.lists:hover {
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
}
.flight {
    width:80px;
  font-size: 22px;
  margin-top: 21px;
  margin-left: 15px;
  text-align: center;
  color: rgba(54, 49, 49, 0.815);
}
.company {
    width:80px;
    font-size: 14px;
  margin-top: 3px;
  margin-left: 15px;
  text-align: center;
  color: rgba(92, 201, 255, 0.836);
}
.dTime {
    width: 120px;
  font-size: 20px;
  margin-top: 14px;
  text-align: right;
  color: rgb(0, 0, 0);
}
.dCity {
    width:120px;
    font-size: 12px;
  margin-top: 3px;
  text-align: right;
  color: rgba(100, 100, 100, 0.692);
}
.divid {
    width: 100px;
  font-size: 18px;
  margin-top: 21px;
  font-weight:bolder;
  text-align: center;
  color: rgba(105, 105, 105, 0.349);
}
.cabin{
    width:100px;
    font-size: 14px;
  text-align: center;
  color: rgba(66, 191, 253, 0.733);
}
.aTime {
    width: 120px;
  font-size: 20px;
  margin-top: 14px;
  text-align: left;
  color: rgb(0, 0, 0);
}
.aCity {
    width:120px;
    font-size: 12px;
  margin-top: 3px;
  text-align: left;
  color: rgba(100, 100, 100, 0.692);
}
.price{
    width: 110px;
    font-size: 30px;
    /* font-weight: bold; */
    color: rgb(66, 191, 253);
    text-align: center;
  margin-top: 24px;
}
</style>