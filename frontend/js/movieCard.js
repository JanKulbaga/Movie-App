export default function movieCard(movie) {
  const { title, vote_average, path_to_image } = movie;
  const cardDiv = document.createElement("div");
  cardDiv.classList.add("movie-card");

  const image = document.createElement("img");
  image.src = path_to_image;
  image.alt = title;
  image.loading = "lazy";

  const movieTitle = document.createElement("h4");
  movieTitle.classList.add("movie-title");
  movieTitle.textContent = title;

  const movieInfo = document.createElement("div");
  movieInfo.classList.add("movie-info");

  const voteAverage = document.createElement("div");
  voteAverage.classList.add("vote-average");
  voteAverage.classList.add(voteAverageColor(vote_average));
  voteAverage.textContent = vote_average;

  cardDiv.append(image);
  movieInfo.append(movieTitle);
  movieInfo.append(voteAverage);
  cardDiv.append(movieInfo);
  return cardDiv;
}

function voteAverageColor(voteAverage) {
  if (voteAverage >= 7.5) {
    return "green";
  } else if (voteAverage >= 5) {
    return "orange";
  }
  return "red";
}
