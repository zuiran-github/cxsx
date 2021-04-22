<template>
    <div class="schedule">
        暂无行程页面！
    </div>
</template>

<script>
    import scrollBar from '../components/scrollBar.vue'
  export default {
    components:{
      'scrBar':scrollBar
    },
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style scoped>

</style>