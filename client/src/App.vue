<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/pdf1">PDF1</router-link> |
      <router-link to="/pdf2">PDF2</router-link>
    </div>
    <div v-if="flag"><PDFJSViewer :path="`${path}`" :fileName="`${name}`" /></div>
    <!-- <div>
      <PDFJSViewer
        :path="`lib/pdfjs-2.5.207-dist/web/viewer.html`"
        :fileName="`my-pdf-file.pdf`"
      />
    </div> -->
    <router-view />
  </div>
</template>

<style>
#app {
  margin-top: 60px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

#nav {
  text-align: center;
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<script>
import PDFJSViewer from "./components/PDFJSViewer.vue";

console.log("Test");

export default {
  name: "app",
  components: {
    PDFJSViewer,
  },
  data() {
    return {
      flag: false,
      name: "my-pdf-file.pdf", // change which pdf file loads
      path: "lib/pdfjs-2.5.207-dist/web/viewer.html", // path of the PDF.js viewer.html
    };
  },
};

console.log("Test 3");
</script>
