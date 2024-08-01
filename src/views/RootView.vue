<script setup lang="ts">
import MessageBox from "@/components/MessageBox.vue";
</script>

<template>
  <div id="top">
    <div id="message-container">
      <MessageBox message="はろー テストテスト" />
    </div>
    <div id="chatbox-container">
      <input id="chatbox" />
    </div>
  </div>
</template>

<style>
#top {
  background-color: var(--f-color);
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

#message-container {
  width: 100%;
}

#chatbox-container {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

#chatbox {
  margin: 40px;
  width: 60%;
  border: none;
  outline: none;
  border-radius: 15px;
  background-color: var(--s-color);
  color: var(--t-color);
  padding: 10px;
  font-size: large;
  transition: all 0.3s ease;
  box-shadow: 0 0 4px var(--s-color);
}

#chatbox:focus {
  box-shadow: 0 0 4px var(--t-color);
}
</style>
