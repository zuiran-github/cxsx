<template>
  <div id="app">
    <!-- <navbar></navbar> -->
    <router-view></router-view>
  </div>
</template>

<script>
import navbar from './components/NavBar.vue'
import scrollBar from './components/scrollBar.vue'
  export default {
    name: 'app',
    components:{
    'navbar':navbar
    // 'scrollbar':scrollBar
  },
  
  beforeCreate() {
    document
      .querySelector("body")
      .setAttribute("style", "background-color:rgba(191, 218, 217, 0.24);");
  },
  beforeDestroy() {
    document.querySelector("body").setAttribute("style", "background-color:''");
  },
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>