import movieCard from "./movieCard.js";
import showModal from "./movieModal.js";

const API_URL = "http://127.0.0.1:8080/api/v1/";
const SEARCH_API_URL = "http://127.0.0.1:8080/api/v1/movies?search=";

const movieContainer = document.querySelector("[data-movie-container]");
const form = document.querySelector("[data-form]");
const search = document.querySelector("[data-search]");
const buttons = document.querySelectorAll("[data-button]");
const buttonsContainer = document.querySelector("[data-buttons-container]");
const paginationContainer = document.querySelector(
  "[data-pagination-container]"
);
const paginationButtons = document.querySelectorAll("[data-pagination-button]");

const endPoints = {
  popular: "popular",
  "top rated": "top_rated",
  alphabetical: "alphabetical",
  "reverse alphabetical": "reverse_alphabetical",
};

let endPointName = endPoints.popular;
let pageNumber = 1;

getMovies(`${API_URL}${endPointName}?page=${pageNumber}`);

async function getMovies(apiUrl) {
  const response = await fetch(apiUrl);
  if (response.ok) {
    const data = await response.json();
    const movies = data.results;
    showMovies(movies);
  }
}

function showMovies(movies) {
  movieContainer.innerHTML = "";
  movies.forEach((movie) => {
    const movieCardEl = movieCard(movie);
    movieCardEl.addEventListener("click", () => showModal(movie));
    movieContainer.append(movieCardEl);
  });
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  paginationContainer.style.display = "none";
  buttonsContainer.style.display = "none";
  getMovies(`${SEARCH_API_URL}${search.value}`);
});

buttons.forEach((button) => {
  button.addEventListener("click", (e) => handleButtonClick(e));
});

paginationButtons.forEach((paginationButton) => {
  paginationButton.addEventListener("click", (e) =>
    handlePaginationButtonClick(e)
  );
});

function handleButtonClick(e) {
  endPointName = e.target.innerText.toLowerCase();
  updateActiveButton(e.target, "[data-button].active");
  getMovies(`${API_URL}${endPoints[endPointName]}?page=${pageNumber}`);
}

function handlePaginationButtonClick(e) {
  pageNumber = e.target.innerText;
  updateActiveButton(e.target, "[data-pagination-button].active");
  getMovies(`${API_URL}${endPoints[endPointName]}?page=${pageNumber}`);
}

function updateActiveButton(button, currentButton) {
  const currentButtonEl = document.querySelector(currentButton);
  currentButtonEl.classList.remove("active");
  button.classList.add("active");
}
