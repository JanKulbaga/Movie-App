export default function showModal(movie) {
  const { title, vote_average, path_to_image, genres, length, description } =
    movie;

  const movieModalCloseButton = document.createElement("div");
  movieModalCloseButton.classList.add("movie-modal-close-button");
  movieModalCloseButton.innerHTML = "&times;";

  const movieModalBg = document.createElement("div");
  movieModalBg.classList.add("movie-modal-bg");

  const movieModal = document.createElement("div");
  movieModal.classList.add("movie-modal");

  const movieModalTop = document.createElement("div");
  movieModalTop.classList.add("movie-modal-top");

  const movieModalImage = document.createElement("img");
  movieModalImage.classList.add("movie-modal-image");
  movieModalImage.src = path_to_image;
  movieModalImage.alt = title;
  movieModalImage.loading = "lazy";

  const movieModalInfo = document.createElement("div");
  movieModalInfo.classList.add("movie-modal-info");

  const voteAverage = document.createElement("div");
  voteAverage.innerText = vote_average;
  voteAverage.classList.add("vote-average");
  voteAverage.classList.add(voteAverageColor(vote_average));

  const movieModalTitle = document.createElement("h1");
  movieModalTitle.innerText = title;
  movieModalTitle.classList.add("movie-modal-title");

  const movieModalTime = document.createElement("div");
  movieModalTime.innerText = `${length} min`;

  const movieModalGenres = document.createElement("div");
  movieModalGenres.classList.add("movie-modal-genres");

  for (let i = 0; i < genres.split(" ").length; i++) {
    const movieModalBtn = document.createElement("button");
    movieModalBtn.innerText = genres.split(" ")[i];
    movieModalBtn.classList.add("btn");
    movieModalGenres.append(movieModalBtn);
  }

  const movieModalDescription = document.createElement("div");
  movieModalDescription.classList.add("movie-modal-description");

  const movieModalDescriptionTitle = document.createElement("h4");
  movieModalDescriptionTitle.innerText = "Description";
  movieModalDescriptionTitle.classList.add("movie-modal-description-title");

  const movieModalDescriptionText = document.createElement("p");
  movieModalDescriptionText.innerText = description;
  movieModalDescriptionText.classList.add("movie-modal-description-text");

  movieModalDescription.append(movieModalDescriptionTitle);
  movieModalDescription.append(movieModalDescriptionText);

  movieModalInfo.append(voteAverage);
  movieModalInfo.append(movieModalTitle);
  movieModalInfo.append(movieModalTime);

  movieModalTop.append(movieModalImage);
  movieModalTop.append(movieModalInfo);

  movieModal.append(movieModalCloseButton);
  movieModal.append(movieModalTop);
  movieModal.append(movieModalGenres);
  movieModal.append(movieModalDescription);
  movieModalBg.append(movieModal);
  document.body.append(movieModalBg);

  document
    .querySelector(".movie-modal-close-button")
    .addEventListener("click", () => {
      document.querySelector(".movie-modal-bg").remove();
    });
}

function voteAverageColor(voteAverage) {
  if (voteAverage >= 7.5) {
    return "green";
  } else if (voteAverage >= 5) {
    return "orange";
  }
  return "red";
}
