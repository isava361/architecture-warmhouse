package main

import (
	"fmt"
	"math"
	"math/rand"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

type TemperatureResponse struct {
	Value       float64   `json:"value"`
	Unit        string    `json:"unit"`
	Timestamp   time.Time `json:"timestamp"`
	Location    string    `json:"location"`
	Status      string    `json:"status"`
	SensorID    string    `json:"sensor_id"`
	SensorType  string    `json:"sensor_type"`
	Description string    `json:"description"`
}

func generateFakeTemperature(sensorID, location string) TemperatureResponse {
	if location == "" {
		if sensorID != "" {
			location = "Room-" + sensorID
		} else {
			location = "Unknown Location"
		}
	}

	if sensorID == "" {
		sensorID = randomID()
	}

	return TemperatureResponse{
		Value:       randomTemp(),
		Unit:        "Celsius",
		Timestamp:   time.Now().UTC(),
		Location:    location,
		Status:      "ok",
		SensorID:    sensorID,
		SensorType:  "temperature",
		Description: "Simulated temperature sensor for " + location + ".",
	}
}

func randomID() string {
	return fmt.Sprintf("%d", rand.Intn(999)+1)
}

func randomTemp() float64 {
	return math.Round((18+rand.Float64()*7.5)*100) / 100
}

func getTemperatureByID(c *gin.Context) {
	sensorID := c.Param("sensor_id")
	data := generateFakeTemperature(sensorID, "")
	c.JSON(http.StatusOK, data)
}

func getTemperatureByLocation(c *gin.Context) {
	location := c.Query("location")
	if location == "" {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Location parameter is required"})
		return
	}
	data := generateFakeTemperature("", location)
	c.JSON(http.StatusOK, data)
}

func main() {
	rand.Seed(time.Now().UnixNano())
	r := gin.Default()

	r.GET("/temperature/:sensor_id", getTemperatureByID)
	r.GET("/temperature", getTemperatureByLocation)
	r.GET("/", func(c *gin.Context) {
		c.String(http.StatusOK, "<h1>Temperature API Simulator is running</h1>")
	})

	r.Run(":8081")
}
