<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png" />
        <Home></Home>
    </div>
</template>

<script>
import Home from "./components/Home.vue";

export default {
    name: "App",
    components: {
        Home
    }
};
</script>

<style>
#app {
    text-align: center;
    margin-top: 60px;
}
</style>
