<template>
    <div class="blank"></div>
</template>

<script>
export default {
    beforeRouteEnter(to, from, next) {
        var query1=from.query;
    next((xq) => {
    //要注意，必须使用this.$router.replace而非this.$router.push
    //如果使用的是this.$router.push会导致，进入过空白页之后，通过浏览器的后退键，无法实现页面后退的bug现象
      xq.$router.replace({path:from.path,query:query1});
    });
  },
}
</script>