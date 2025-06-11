#include "json.hpp"
#include <curl/curl.h>
#include <iostream>
#include <string>

using namespace std;
using json = nlohmann::json;

const string API_KEY = "3f371c6dfeee604999e1a244";

static size_t write_callback(void* contents, size_t size, size_t nmemb, void* vs) {
    string* s = (string*)vs;
    s->append((char*)contents, size * nmemb);
    return size * nmemb;
}

enum state_e {
    CHOOSING_CURRENCY,
    CHOOSING_SUM,
    CHOOSING_TARGET_CURRENCY
};

struct currency {
    string name;
    string sign;
    string code;
};

const currency  currencies[] = {
    {"Rubli", "₽", "RUB"},
    {"Złote", "zł", "PLN"},
    {"Dolary", "$", "USD"},
    {"Euro", "€", "EUR"},
    {"Funty", "£", "GBP"}
};
int currencies_count = sizeof(currencies) / sizeof(currencies[0]);

void output_currencies() {
    for (int i = 0; i < currencies_count; i++) {
        cout << i + 1 << ") " << currencies[i].name << ' ' << currencies[i].sign << '\n';
    }
}

double calculate_exchange_rate(int from, int to) {
    string url = "https://v6.exchangerate-api.com/v6/" + API_KEY + "/pair/" + currencies[from].code + "/" + currencies[to].code;
    CURL* curl = curl_easy_init();
    string response;
    
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0L);
        curl_easy_perform(curl);
        curl_easy_cleanup(curl);

        auto dane_json = json::parse(response);
        double rate = dane_json["conversion_rate"];
        return rate;
    }

    return 0.0;
}

int main() {
    system("chcp 65001 > nul");
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);

    bool leave = false;
    state_e state = CHOOSING_CURRENCY;

    int initial_currency = 0;
    int target_currency = 0;
    float amount_to_convert = 0.0;

    while (!leave) {
        switch (state) {
            case CHOOSING_CURRENCY: {
                cout << "Wybierz walutę z której chcesz przeliczyć:\n";
                output_currencies();
                string inp;
                while (true) {
                    cout << "Wpisz numer: ";
                    getline(cin, inp);
                    try {
                        int num = stod(inp);
                        if (num < 1 || num > currencies_count) {
                            throw invalid_argument("");
                        }
                        initial_currency = num - 1;
                        break;
                    } catch(const invalid_argument& e) {
                        cout << "Błędne dane wejściowe.\n";
                    }
                }
                state = CHOOSING_SUM;
                break;
            }
            case CHOOSING_SUM: {
                string inp;
                while (true) {
                    cout << "Wpisz sumę: ";
                    getline(cin, inp);
                    try {
                        float num = stof(inp);
                        if (num < 0.0) {
                            throw invalid_argument("");
                        }
                        amount_to_convert = num;
                        break;
                    } catch(const invalid_argument& e) {
                        cout << "Błędne dane wejściowe.\n";
                    }
                }
                state = CHOOSING_TARGET_CURRENCY;
                break;
            }
            case CHOOSING_TARGET_CURRENCY: {
                cout << "Wybierz walutę na którą chcesz przeliczyć:\n";
                output_currencies();
                string inp;
                while (true) {
                    cout << "Wpisz numer: ";
                    getline(cin, inp);
                    try {
                        int num = stod(inp);
                        if (num < 1 || num > currencies_count) {
                            throw invalid_argument("");
                        }
                        target_currency = num - 1;
                        break;
                    } catch(const invalid_argument& e) {
                        cout << "Błędne dane wejściowe.\n";
                    }
                }
                double rate = calculate_exchange_rate(initial_currency, target_currency);
                cout << "Przeliczona kwota waluty (" << (initial_currency != 1 ? "z" : "ze") << " " << currencies[initial_currency].sign << " na " << currencies[target_currency].sign <<  "): " << amount_to_convert * rate << ' ' << currencies[target_currency].sign << '\n';
                state = CHOOSING_CURRENCY;
                break;
            }
        }
    }

    return 0;
}