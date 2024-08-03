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
  justify-content: flex-start;
  align-items: center;
  padding: 15px;
  padding-left: 20px;
  padding-right: 20px;
  border-top: 1px solid var(--s-color);
  border-bottom: 1px solid var(--s-color);
  width: 90%;
}

#messagebox p {
  display: block;
  margin: 0;
  color: var(--t-color);
}
</style>
