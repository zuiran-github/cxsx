<template>
  <el-carousel height="100" class="scrollBar" ref="carousel" @click.native="linkTo">
           <!-- <el-carousel-item class="lun_img" v-for="item in imgs" v-bind:key="item.url" >
             <img :src="item.url" style="height:100%;width:100%;"/>
           </el-carousel-item> -->
           <el-carousel-item class="lun_img">
             <el-card class="searchBar">
          <el-form
            :model="ruleForm"
            :rules="rules"
            ref="ruleForm"
            label-width="100px"
          >
            <el-row>
              <el-col :span="10" :offset="1">
                <el-form-item label="出发地" prop="departure">
                  <el-input v-model="ruleForm.departure"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="10" :offset="1">
                <el-form-item label="目的地" prop="destination">
                  <el-input v-model="ruleForm.destination"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="10" :offset="1">
                <el-form-item label="出发日期" prop="date1">
                  <el-date-picker
                    type="date"
                    placeholder="选择日期"
                    v-model="ruleForm.date1"
                    style="width: 100%"
                    :picker-options="pickeroptions"
                  ></el-date-picker>
                </el-form-item>
              </el-col>
              <el-col :span="10" :offset="2">
                <el-form-item label="返回日期" v-show="false">
                  <el-date-picker
                    type="date"
                    placeholder="选择日期"
                    v-model="ruleForm.date2"
                    style="width: 100%"
                    :picker-options="pickeroptions"
                  ></el-date-picker>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="22" :offset="1">
                <!-- :offset="3" -->
                <el-form-item label="筛选类型">
                  <el-row>
                    <el-radio-group
                      v-model="ruleForm.radio"
                      @change="showTrains"
                    >
                      <el-radio :label="1">全部</el-radio>
                      <el-radio :label="2">火车</el-radio>
                      <el-radio :label="3">飞机</el-radio>
                    </el-radio-group>
                  </el-row>
                  <el-row>
                    <el-form-item prop="type">
                      <el-checkbox-group
                        v-model="ruleForm.type"
                        v-show="ruleForm.isSeen"
                      >
                        <el-checkbox label="G-高铁" name="type"></el-checkbox>
                        <el-checkbox label="D-动车" name="type"></el-checkbox>
                        <el-checkbox label="Z-直达" name="type"></el-checkbox>
                        <el-checkbox label="T-特快" name="type"></el-checkbox>
                        <el-checkbox label="K-快速" name="type"></el-checkbox>
                        <el-checkbox label="其他" name="type"></el-checkbox>
                      </el-checkbox-group>
                    </el-form-item>
                  </el-row>
                </el-form-item>
              </el-col>
            </el-row>
            <el-form-item>
              <el-button type="primary" @click="submitForm()">搜索</el-button>
              <!-- <el-button @click="resetForm('ruleForm')">重置</el-button> -->
            </el-form-item>
          </el-form>
        </el-card>
        
             <img src="../assets/images/bg4.jpg" style="height:100%;width:100%;"/>
           </el-carousel-item>
         </el-carousel>
</template>

<script>

export default {
    // data(){
    //     return{
    //         imgs:[
    //             {url: require('../assets/images/bg4.jpg'), link: '/'},
    //     {url: require('../assets/images/bg1.jpg'), link: '/ticket'},
    //     {url: require('../assets/images/bg2.jpg'), link: '/hotel'},
    //     {url: require('../assets/images/bg5.jpg'), link: '/schedule'},
    //     {url: require('../assets/images/bg3.jpg'), link: '/discount'}
    //     ]
    //     }
    // },
    methods: {
    linkTo () {
      let activeIndex = this.$refs.carousel.activeIndex
      this.$router.push({path:this.imgs[activeIndex].link})
    },
    showTrains(numlab) {
      console.log("changed!");
      if (numlab == 2) {
        this.ruleForm.isSeen = true;
        this.rules.type.required = true;
      } else {
        this.ruleForm.isSeen = false;
        //this.rules.type.required = false;
        this.ruleForm.type = [];
      }
    },

    submitForm() {
      // console.log(this.ruleForm);
      this.$router.push({
        name: "tickets",

        //query/
        query: {
          departure: this.ruleForm.departure,
          destination: this.ruleForm.destination,
          date1: String(this.ruleForm.date1),
          date2: String(this.ruleForm.date2),
          radio: this.ruleForm.radio,
          type: this.ruleForm.type,
        },
      });
      console.log(String(this.ruleForm.date1));
      // console.log("submit! post");
      // // axios.post('http://127.0.0.1:8000/tickets.json',this.formName).then(res => {//get()中的参数要与mock.js文件中的Mock.mock()配置的路由保持一致
      // //           this.$axios.post('api/tickets/',this.formName).then((res) => {//get()中的参数要与mock.js文件中的Mock.mock()配置的路由保持一致
      // this.$axios({
      //   method: "post",
      //   url: "api/tickets",
      //   data: {
      //     departure: this.ruleForm.departure,
      //     destination: this.ruleForm.destination,
      //     goDate: this.ruleForm.date1,
      //     backDate: this.ruleForm.date2,
      //     trainOrPlane: this.ruleForm.radio,
      //     trainType: this.ruleForm.type,
      //   },
      // })
      //   .then((res) => {
      //     console.log(res.data); //在console中看到数据
      //     console.log("ok");
      //   })
      //   .catch((res) => {
      //     alert("请求失败，请重试！");
      //   });
    },

    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    showchange() {
      this.show = !this.show;
    },
  },

  mounted() {
    this.showchange();
  },

  data() {
    return {
      show: false,
      pickeroptions: {
        disabledDate(v) {
          return v.getTime() < new Date().getTime();
        },
      },

      ruleForm: {
        departure: "",
        destination: "",
        date1: "",
        date2: "",
        radio: 1,
        type: [],
        isSeen: false,
      },

      rules: {
        departure: [
          { required: true, message: "请输入出发地", trigger: "blur" },
          //{ min: 3, max: 5, message: "长度在 3 到 5 个字符", trigger: "blur" },
        ],
        destination: [
          { required: true, message: "请输入目的地", trigger: "blur" },
        ],
        date1: [
          {
            type: "date",
            required: true,
            message: "请选择日期",
            trigger: "change",
          },
        ],
        date2: [
          {
            type: "date",
            required: false,
            message: "请选择日期",
            trigger: "change",
          },
        ],
        type: [
          {
            type: "array",
            required: false, //不验证了，没选就默认全选吧
            message: "请至少选择一种类型",
            trigger: "change",
          },
        ],
      },
    };
  },
  
}
</script>


<style>
  /* .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  } */
  .searchBar {
    position: absolute;
    width: 75%;
    height:75%;
  }
</style>