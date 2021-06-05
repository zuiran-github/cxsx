<template>
  <el-menu
      :default-active="$route.path"
      class="navbar"
      background-color="#03A9F4"
      text-color="#FFFFFF"
      active-text-color="#fde74cff"
      mode="horizontal"
      @select="jump">
      <el-menu-item index="1">
        <i class="el-icon-s-home"></i>
        <span slot="title">首页</span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-truck"></i>
        <span slot="title">出行交通</span>
      </el-menu-item>
      <el-menu-item index="3">
        <i class="el-icon-office-building"></i>
        <span slot="title">酒店搜索</span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-s-ticket"></i>
        <span slot="title">优惠查询</span>
      </el-menu-item>
    </el-menu>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: "2",
    };
  },
  // props:{
  //   activeIndex: {default:'2'},
  // },
  methods: {
    jump(index,indexPath){
          this.activeIndex=index;
        if(index == "1"){
          this.$router.push("/");
        }else{
          if(index == "2"){
            this.$router.push("/ticket");
          }else{
            if(index=="3"){
              this.$router.push("/hotel");
            }else{
              this.$router.push("/discount");
            }
          }
        }
    }
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>