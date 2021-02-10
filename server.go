package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	body, _ := ioutil.ReadAll(r.Body)
	fmt.Fprintf(w, "%s\n", string(body))
}

func main() {
	// https://sandbox.bluebutton.cms.gov/v1/fhir/Patient/?patient=20140000008325
	http.HandleFunc("/", handler)

	host := ""
	port := "3456"
	addr := fmt.Sprintf("%s:%s", host, port)
	log.Printf("Serving on %s", addr)
	log.Fatal(http.ListenAndServe(addr, nil))
}
