<script setup lang="ts">
defineProps(["message"]);
</script>

<template>
  <div id="messagebox">
    <p>{{ message }}</p>
  </div>
</template>

<style>
#messagebox {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  padding: 5px;
  padding-left: 20px;
  padding-right: 20px;
  background-color: var(--s-color);
  border-radius: 15px;
  margin: 10px;
}

#messagebox p {
  display: block;
  margin: 0;
  color: var(--t-color);
}
</style>
