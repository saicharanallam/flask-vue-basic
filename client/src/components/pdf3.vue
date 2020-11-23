<template>
  <div>
    <p>How are ya?</p>
    <h1>pdf.pdf render in web with clickable signing block</h1>
    <canvas id="the-canvas"></canvas>
  </div>
</template>
<script>
import pdfjsLib from "pdfjs-dist/build/pdf";

export default {
  methods: {
    renderCanvas() {
      const pdfData = "./new.pdf";
      // const pdfjsLib = window["lib/pdfjs-2.5.207-dist/build/pdf"];
      // const loadingTask = pdfjsLib.getDocument({ data: pdfData });
      const loadingTask = pdfjsLib.getDocument("./new.pdf");
      const libFile = "lib/pdfjs-2.5.207-dist/build/pdf.worker.js";
      console.log(pdfData);

      // The workerSrc property shall be specified.
      pdfjsLib.GlobalWorkerOptions.workerSrc = libFile;

      function getMousePos(canvas, event) {
        const rect = canvas.getBoundingClientRect();
        return {
          x: event.clientX - rect.left,
          y: event.clientY - rect.top,
        };
      }
      function isInside(pos, rect) {
        return (
          pos.x > rect.x
          && pos.x < rect.x + rect.width
          && pos.y < rect.y + rect.height
          && pos.y > rect.y
        );
      }
      // Using DocumentInitParameters object to load binary data.
      loadingTask.promise.then(
        (pdf) => {
          console.log("PDF loaded");

          // Fetch the first page
          const pageNumber = 1;
          pdf.getPage(pageNumber).then((page) => {
            console.log("Page loaded");

            const scale = 1.0;
            const viewport = page.getViewport({ scale });

            // Prepare canvas using PDF page dimensions
            const canvas = document.getElementById("the-canvas");
            const context = canvas.getContext("2d");
            canvas.height = viewport.height;
            canvas.width = viewport.width;

            // Render PDF page into canvas context
            const renderContext = {
              canvasContext: context,
              viewport,
            };
            const renderTask = page.render(renderContext);
            renderTask.promise.then(() => {
              console.log("Page rendered");
              const rect = {
                x: 60,
                y: 630,
                width: 120,
                height: 40,
              };
              // const context = canvas.getContext("2d");
              const path = new Path2D();
              path.rect(60, 630, 120, 40);
              path.closePath();

              // draw your shape data to the context
              context.fillStyle = "#FFFFFF";
              context.fillStyle = "rgba(225,225,225,0.5)";
              context.fill(path);
              context.lineWidth = 2;
              context.strokeStyle = "#000000";
              context.stroke(path);

              // Binding the click event on the canvas
              canvas.addEventListener(
                "click",
                (evt) => {
                  const mousePos = getMousePos(canvas, evt);

                  if (isInside(mousePos, rect)) {
                    console.log(mousePos);
                    alert("clicked inside rect");
                  } else {
                    console.log(mousePos);

                    alert("clicked outside rect");
                  }
                },
                false,
              );
              const ctx = canvas.getContext("2d");

              ctx.font = "14 Arial";
              ctx.strokeText("Click to Sign", 70, 657);
            });
          });
        },
        (reason) => {
          // PDF loading error
          console.error(reason);
        },
      );
    },
  },
  created() {
    this.renderCanvas();
  },
};
</script>
