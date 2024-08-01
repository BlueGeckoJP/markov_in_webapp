<script setup lang="ts">
import axios from "axios";
import { onMounted } from "vue";

async function updateText() {
  let textElement = document.getElementById("text");
  if (textElement) {
    while (true) {
      await axios.get("/api").then(async (res) => {
        textElement.innerHTML += res.data;
      });
      await autoScroll();
      await sleep(500);
    }
  }
}

async function autoScroll() {
  const container = document.getElementById("text-container");
  const target = document.getElementById("text");

  const containerRect = container!.getBoundingClientRect();
  const targetRect = target!.getBoundingClientRect();

  if (targetRect.bottom > containerRect.bottom) {
    container!.scrollTo({
      top: target!.offsetHeight,
      behavior: "smooth",
    });
  }
}

function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

onMounted(() => {
  updateText();
});
</script>

<template>
  <div id="top">
    <div id="text-container">
      <p id="text"></p>
    </div>
  </div>
</template>

<style>
body {
  background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  background-size: 400% 400%;
  animation: gradient-background 5s ease infinite;
  overflow: hidden;
}

@keyframes gradient-background {
  0% {
    background-position: 0 100%;
  }
  50% {
    background-position: 100% 0%;
  }
  100% {
    background-position: 0% 100%;
  }
}

p {
  margin: 0;
  color: var(--main-color);
  font-size: large;
}

#top {
  width: 100%;
  height: 100vh;
  margin: 0;
}

#text-container {
  height: calc(100% - 10px);
  margin: 5px;
  padding: 5px;
  border: dashed 2px var(--main-color);
  overflow: hidden;
}
</style>
