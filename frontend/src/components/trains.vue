<template>
    <div class="trains">
        <el-checkbox-group v-model="type">
                <el-checkbox label="G-高铁" name="type"></el-checkbox>
                <el-checkbox label="D-动车" name="type"></el-checkbox>
                <el-checkbox label="Z-直达" name="type"></el-checkbox>
                <el-checkbox label="T-特快" name="type"></el-checkbox>
                <el-checkbox label="K-快速" name="type"></el-checkbox>
                <el-checkbox label="其他" name="type"></el-checkbox>
            </el-checkbox-group>
    </div>
</template>

<script>
  export default {
    data() {
      return {
        type:[]
      };
    }
  }
</script>

<style scoped>

</style>