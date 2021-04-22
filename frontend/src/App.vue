<template>
  <div id="app">
    <!-- <scrollbar></scrollbar> -->
    <router-view></router-view>
  </div>
</template>

<script>
// import NavBar from './components/NavBar.vue'
import scrollBar from './components/scrollBar.vue'
  export default {
    name: 'app',
    components:{
    // 'navbar':NavBar
    'scrollbar':scrollBar
  }
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