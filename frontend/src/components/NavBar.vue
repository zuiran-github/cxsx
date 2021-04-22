<template>
  <el-menu
    :default-active="activeIndex"
    class="NavBar"
    mode="horizontal"
    @select="handleSelect"
  >
  <el-menu-item index="0">
      <router-link to="/">首页</router-link>
    </el-menu-item>
    <el-menu-item index="1">
      <router-link to="/ticket">火车票&机票</router-link>
    </el-menu-item>
    <el-menu-item index="2">
      <router-link to="/hotel">酒店查询</router-link>
    </el-menu-item>
    <el-menu-item index="3">
      <router-link to="/schedule">行程推荐</router-link>
    </el-menu-item>
    <el-menu-item index="4">
      <router-link to="/discount">优惠搜索</router-link>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  // data() {
  //   return {
  //     activeIndex: "0",
  //     activeIndex2: "0",
  //   };
  // },
  props:{
    activeIndex: {default:"0"},
    activeIndex2:{default: "0"},
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>