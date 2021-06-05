<template>
  <div class="newtrain">
    <div class="lists" @click="jump()">
      <el-col>
        <div class="flight">{{ trainID }}</div>
      </el-col>
      <el-col>
        <div class="dTime">
          {{
            dStation
          }}
        </div>
        <div class="dCity">{{ dtime }}</div>
      </el-col>
      <el-col>
        <div class="divid">————</div>
        <div class="cabin">{{ "历时"+during }}</div>
      </el-col>
      <el-col>
        <div class="aTime">
          {{
            aStation
          }}
        </div>
        <div class="aCity">{{ atime }}</div>
      </el-col>
      <el-col>
        <div class="price">
          <el-row v-show="hasShang">
              <el-tag effect="dark" size="mini" type="danger">商务座</el-tag>
              {{ shangwu }}</el-row>
          <el-row v-show="hasYi">
              <el-tag effect="dark" size="mini" type="warning">一等座</el-tag>
              {{ yidengzuo }}</el-row>
          <el-row v-show="hasEr">
              <el-tag effect="dark" size="mini" type="success">二等座</el-tag>
              {{ erdengzuo }}</el-row>
          <el-row v-show="hasGao">
              <el-tag effect="dark" size="mini" type="danger">高级软卧</el-tag>
              {{ gaojiruanwo }}</el-row>
          <el-row v-show="hasRuanWo">
              <el-tag effect="dark" size="mini" type="danger">软卧</el-tag>
              {{ ruanwo }}</el-row>
          <el-row v-show="hasDong">
              <el-tag effect="dark" size="mini" type="danger">动卧</el-tag>
              {{ dongwo }}</el-row>
          <el-row v-show="hasYingWo">
              <el-tag effect="dark" size="mini" type="warning">硬卧</el-tag>
              {{ yingwo }}</el-row>
          <el-row v-show="hasRuanZuo">
              <el-tag effect="dark" size="mini" type="success">软座</el-tag>
              {{ ruanzuo }}</el-row>
          <el-row v-show="hasYingZuo">
              <el-tag effect="dark" size="mini" type="success">硬座</el-tag>
              {{ yingzuo }}</el-row>
          <el-row v-show="hasWu">
              <el-tag effect="dark" size="mini" type="info">无座</el-tag>
              {{ wuzuo }}</el-row>
          <el-row v-show="hasQi">
              <el-tag effect="dark" size="mini" type="info">其他</el-tag>
              {{ qita }}</el-row>
        </div>
      </el-col>
      <el-col>
        <div class="lowprice">{{"¥"+price}}</div>
      </el-col>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    trainID: {
      default: "暂无车次",
    },
    dStation: {
      default: "出发站",
    },
    aStation: {
      default: "到达站",
    },
    dtime: {
      default: "",
    },
    atime: {
      default: "",
    },
    during: {
      default: "",
    },
    shangwu: {
      default: "",
    },
    yidengzuo: {
      default: "",
    },
    erdengzuo: {
      default: "",
    },
    gaojiruanwo: {
      default: "",
    },
    ruanwo: {
      default: "",
    },
    dongwo: {
      default: "",
    },
    yingwo: {
      default: "",
    },
    ruanzuo: {
      default: "",
    },
    yingzuo: {
      default: "",
    },
    wuzuo: {
      default: "",
    },
    qita: {
      default: "",
    },
    tzurl: {
      default: "",
    },
    price:{
      default:0,
    }
  },
  data() {
    return {
      hasShang: false,
      hasYi: false,
      hasEr: false,
      hasGao: false,
      hasRuanWo: false,
      hasDong: false,
      hasYingWo: false,
      hasRuanZuo: false,
      hasYingZuo: false,
      hasWu: false,
      hasQi: false,
    };
  },
  methods: {
    jump() {
      window.open(this.tzurl);
    },
    showWhat() {
      if (!this.shangwu == "") {
        this.hasShang = true;
      }
      if (!this.yidengzuo == "") {
        this.hasYi = true;
      }
      if (!this.erdengzuo == "") {
        this.hasEr = true;
      }
      if (!this.gaojiruanwo == "") {
        this.hasGao = true;
      }
      if (!this.ruanwo == "") {
        this.hasRuanWo = true;
      }
      if (!this.dongwo == "") {
        this.hasDong = true;
      }
      if (!this.yingwo == "") {
        this.hasYingWo = true;
      }
      if (!this.ruanzuo == "") {
        this.hasRuanZuo = true;
      }
      if (!this.yingzuo == "") {
        this.hasYingZuo = true;
      }
      if (!this.wuzuo == "") {
        this.hasWu = true;
      }
      if (!this.qita == "") {
        this.hasQi = true;
      }
    },
  },

  mounted() {
    this.showWhat();
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
  width: 60px;
  font-size: 22px;
  margin-top: 32px;
  margin-left: 15px;
  text-align: center;
  color: rgba(54, 49, 49, 0.815);
}
.dTime {
  width: 80px;
  font-size: 20px;
  margin-top: 23px;
  text-align: right;
  color: rgb(0, 0, 0);
}
.dCity {
  width: 80px;
  font-size: 15px;
  margin-top: 3px;
  text-align: right;
  color: rgba(100, 100, 100, 0.692);
}
.divid {
  width: 100px;
  font-size: 20px;
  margin-top: 26px;
  font-weight: bolder;
  text-align: center;
  color: rgba(105, 105, 105, 0.349);
}
.cabin {
  width: 100px;
  font-size: 13px;
  text-align: center;
  color: rgba(66, 191, 253, 0.733);
}
.aTime {
  width: 80px;
  font-size: 20px;
  margin-top: 23px;
  text-align: left;
  color: rgb(0, 0, 0);
}
.aCity {
  width: 80px;
  font-size: 15px;
  margin-top: 3px;
  text-align: left;
  color: rgba(100, 100, 100, 0.692);
}
.price {
  width: 80px;
  font-size: 14px;
  /* font-weight: bold; */
  color: rgb(66, 191, 253);
  text-align: left;
  margin-top: 12px;
  margin-left: 20px;
}
.lowprice{
  width: 100px;
    font-size: 30px;
    /* font-weight: bold; */
    color: rgb(66, 191, 253);
    text-align: center;
  margin-top: 24px;
}
</style>