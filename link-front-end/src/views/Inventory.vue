<script setup>
    import { ref, onMounted } from "vue"
    import "./styles/inventory.scss"
    import Card from "../components/Card.vue"

    const items = ref(null)
    const loading = ref(false)

    async function fetchData() {
        try {
            loading.value = true
            const response = await fetch('/apilink/dev/inventario');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            items.value = data; // Assuming the response is an array of items
            console.log(items || "aun no")
        } catch (error) {
            console.error('There was a problem fetching the data:', error);
        } finally {
            loading.value = false
        }
    }
    onMounted(fetchData)
</script>

<template>
    <div>
        <div v-if="loading" class="container">
            Cargandooo...
        </div>
        <div v-else class="container">
            <div v-for="item in items" :key="item._id.$oid">
                <Card :marca="item.marca" :modelo="item.modelo" />
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
    .container {
        display: flex;
        justify-content: center;
        gap: 2rem
    }
</style>
