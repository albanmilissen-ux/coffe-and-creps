<script setup lang="ts">
import { onMounted, ref } from "vue";

const apiMessage = ref("Conectando con la API...");
const apiError = ref(false);

onMounted(async () => {
  try {
    const response = await fetch("/api/health");
    if (!response.ok) {
      throw new Error(`La API respondio con HTTP ${response.status}`);
    }

    const result: { status: string; message: string } = await response.json();
    apiMessage.value = result.message;
  } catch (error) {
    apiMessage.value =
      error instanceof Error
        ? error.message
        : "Error desconocido al conectar con la API.";
    apiError.value = true;
  }
});
</script>

<template>
  <main class="page">
    <section class="card" aria-labelledby="page-title">
      <p class="eyebrow">Cafe, crepas y buenos momentos</p>
      <h1 id="page-title">Coffe <span>&</span> Creps</h1>
      <p class="intro">
        Un espacio acogedor para disfrutar algo rico, preparado al momento.
      </p>
      <div class="api-status" :class="{ 'api-status--error': apiError }" role="status">
        <span class="status-dot" aria-hidden="true"></span>
        {{ apiMessage }}
      </div>
    </section>
  </main>
</template>
