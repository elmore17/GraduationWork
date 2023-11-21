<template>
  <Nav />
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
import Nav from './Nav.vue';
export default {
  name: 'Main',
  components:{
    Nav,
  }
};
</script>

<script setup>
import Home from './Home.vue';
</script>
  