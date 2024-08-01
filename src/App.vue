<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <nav>
    <RouterLink id="routerlink" to="/">Go to Home</RouterLink>
    <RouterLink id="routerlink" to="/infinite"
      >Let's go to the infinite beyond</RouterLink
    >
  </nav>
  <main>
    <RouterView />
  </main>
</template>

<style>
nav {
  height: 30px;
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

#routerlink {
  margin-right: 10px;
  text-align: center;
  font-weight: bold;
  font-size: large;
}
</style>
