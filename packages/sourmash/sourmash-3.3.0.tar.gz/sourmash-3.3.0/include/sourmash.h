/* c bindings to the sourmash library */

#ifndef SOURMASH_H_INCLUDED
#define SOURMASH_H_INCLUDED

#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

enum HashFunctions {
  HASH_FUNCTIONS_MURMUR64_DNA = 1,
  HASH_FUNCTIONS_MURMUR64_PROTEIN = 2,
  HASH_FUNCTIONS_MURMUR64_DAYHOFF = 3,
  HASH_FUNCTIONS_MURMUR64_HP = 4,
};
typedef uint32_t HashFunctions;

enum SourmashErrorCode {
  SOURMASH_ERROR_CODE_NO_ERROR = 0,
  SOURMASH_ERROR_CODE_PANIC = 1,
  SOURMASH_ERROR_CODE_INTERNAL = 2,
  SOURMASH_ERROR_CODE_MSG = 3,
  SOURMASH_ERROR_CODE_UNKNOWN = 4,
  SOURMASH_ERROR_CODE_MISMATCH_KSIZES = 101,
  SOURMASH_ERROR_CODE_MISMATCH_DNAPROT = 102,
  SOURMASH_ERROR_CODE_MISMATCH_MAX_HASH = 103,
  SOURMASH_ERROR_CODE_MISMATCH_SEED = 104,
  SOURMASH_ERROR_CODE_MISMATCH_SIGNATURE_TYPE = 105,
  SOURMASH_ERROR_CODE_NON_EMPTY_MIN_HASH = 106,
  SOURMASH_ERROR_CODE_INVALID_DNA = 1101,
  SOURMASH_ERROR_CODE_INVALID_PROT = 1102,
  SOURMASH_ERROR_CODE_INVALID_CODON_LENGTH = 1103,
  SOURMASH_ERROR_CODE_INVALID_HASH_FUNCTION = 1104,
  SOURMASH_ERROR_CODE_IO = 100001,
  SOURMASH_ERROR_CODE_UTF8_ERROR = 100002,
  SOURMASH_ERROR_CODE_PARSE_INT = 100003,
  SOURMASH_ERROR_CODE_SERDE_ERROR = 100004,
};
typedef uint32_t SourmashErrorCode;

typedef struct ComputeParameters ComputeParameters;

typedef struct KmerMinHash KmerMinHash;

typedef struct Nodegraph Nodegraph;

typedef struct Signature Signature;

/**
 * Represents a string.
 */
typedef struct {
  char *data;
  uintptr_t len;
  bool owned;
} SourmashStr;

ComputeParameters *computeparams_new(void);

void computeparams_free(ComputeParameters *ptr);

uint64_t computeparams_seed(ComputeParameters *ptr);

void computeparams_set_seed(ComputeParameters *ptr, uint64_t seed);

const uint32_t* computeparams_ksizes(ComputeParameters *ptr, uintptr_t *size);

void computeparams_set_ksizes(ComputeParameters *ptr, const uint32_t *ksizes_ptr, uintptr_t insize);

bool computeparams_protein(ComputeParameters *ptr);

void computeparams_set_protein(ComputeParameters *ptr, bool protein);

bool computeparams_dayhoff(ComputeParameters *ptr);

void computeparams_set_dayhoff(ComputeParameters *ptr, bool dayhoff);

bool computeparams_hp(ComputeParameters *ptr);

void computeparams_set_hp(ComputeParameters *ptr, bool hp);

bool computeparams_dna(ComputeParameters *ptr);

void computeparams_set_dna(ComputeParameters *ptr, bool dna);

bool computeparams_track_abundance(ComputeParameters *ptr);

void computeparams_set_track_abundance(ComputeParameters *ptr, bool track);

uint32_t computeparams_num_hashes(ComputeParameters *ptr);

void computeparams_set_num_hashes(ComputeParameters *ptr, uint32_t num);

uint64_t computeparams_scaled(ComputeParameters *ptr);

void computeparams_set_scaled(ComputeParameters *ptr, uint64_t scaled);

uint64_t hash_murmur(const char *kmer, uint64_t seed);

void kmerminhash_add_from(KmerMinHash *ptr, const KmerMinHash *other);

void kmerminhash_add_hash(KmerMinHash *ptr, uint64_t h);

void kmerminhash_add_sequence(KmerMinHash *ptr, const char *sequence, bool force);

void kmerminhash_add_protein(KmerMinHash *ptr, const char *sequence);

void kmerminhash_add_word(KmerMinHash *ptr, const char *word);

double kmerminhash_jaccard(KmerMinHash *ptr, const KmerMinHash *other, bool downsample);

double kmerminhash_similarity(KmerMinHash *ptr, const KmerMinHash *other, bool ignore_abundance, bool downsample);
double kmerminhash_angular_similarity(KmerMinHash *ptr, const KmerMinHash *other, bool ignore_abundance, bool downsample);

uint64_t kmerminhash_count_common(KmerMinHash *ptr, const KmerMinHash *other, bool downsample);

bool kmerminhash_dayhoff(KmerMinHash *ptr);

void kmerminhash_disable_abundance(KmerMinHash *ptr);

void kmerminhash_enable_abundance(KmerMinHash *ptr);

void kmerminhash_free(KmerMinHash *ptr);

void kmerminhash_slice_free(uint64_t *ptr, uintptr_t insize);

uint64_t kmerminhash_get_abund_idx(KmerMinHash *ptr, uint64_t idx);

const uint64_t *kmerminhash_get_abunds(KmerMinHash *ptr);

uintptr_t kmerminhash_get_abunds_size(KmerMinHash *ptr);

uint64_t kmerminhash_get_min_idx(KmerMinHash *ptr, uint64_t idx);

const uint64_t *kmerminhash_get_mins(KmerMinHash *ptr);

void kmerminhash_add_many(KmerMinHash *ptr, const uint64_t *hashes_ptr, uintptr_t insize);

uintptr_t kmerminhash_get_mins_size(KmerMinHash *ptr);

HashFunctions kmerminhash_hash_function(KmerMinHash *ptr);

void kmerminhash_hash_function_set(KmerMinHash *ptr, HashFunctions hash_function);

bool kmerminhash_hp(KmerMinHash *ptr);

uint64_t kmerminhash_intersection(KmerMinHash *ptr, const KmerMinHash *other);

bool kmerminhash_is_protein(KmerMinHash *ptr);

uint32_t kmerminhash_ksize(KmerMinHash *ptr);

uint64_t kmerminhash_max_hash(KmerMinHash *ptr);

SourmashStr kmerminhash_md5sum(KmerMinHash *ptr);

void kmerminhash_merge(KmerMinHash *ptr, const KmerMinHash *other);

bool kmerminhash_is_compatible(const KmerMinHash *ptr, const KmerMinHash *other);

KmerMinHash *kmerminhash_new(uint32_t n,
                             uint32_t k,
                             bool prot,
                             bool dayhoff,
                             bool hp,
                             uint64_t seed,
                             uint64_t mx,
                             bool track_abundance);

uint32_t kmerminhash_num(KmerMinHash *ptr);

void kmerminhash_remove_hash(KmerMinHash *ptr, uint64_t h);

void kmerminhash_remove_many(KmerMinHash *ptr, const uint64_t *hashes_ptr, uintptr_t insize);

uint64_t kmerminhash_seed(KmerMinHash *ptr);

void kmerminhash_set_abundances(KmerMinHash *ptr, const uint64_t *hashes_ptr, const uint64_t *abunds_ptr, uintptr_t insize);

bool kmerminhash_track_abundance(KmerMinHash *ptr);

bool nodegraph_count(Nodegraph *ptr, uint64_t h);

bool nodegraph_count_kmer(Nodegraph *ptr, const char *kmer);

double nodegraph_expected_collisions(Nodegraph *ptr);

void nodegraph_free(Nodegraph *ptr);

Nodegraph *nodegraph_from_buffer(const char *ptr, uintptr_t insize);

Nodegraph *nodegraph_from_path(const char *filename);

uintptr_t nodegraph_get(Nodegraph *ptr, uint64_t h);

uintptr_t nodegraph_get_kmer(Nodegraph *ptr, const char *kmer);

uintptr_t nodegraph_ksize(Nodegraph *ptr);

uintptr_t nodegraph_matches(Nodegraph *ptr, KmerMinHash *mh_ptr);

Nodegraph *nodegraph_new(void);

uintptr_t nodegraph_noccupied(Nodegraph *ptr);

uintptr_t nodegraph_ntables(Nodegraph *ptr);

void nodegraph_save(Nodegraph *ptr, const char *filename);

uint8_t *nodegraph_to_buffer(Nodegraph *ptr, uint8_t compression, uintptr_t *size);

void nodegraph_buffer_free(uint8_t *ptr, uintptr_t insize);

uint64_t *nodegraph_hashsizes(Nodegraph *ptr, uintptr_t *size);

void nodegraph_update(Nodegraph *ptr, Nodegraph *optr);

void nodegraph_update_mh(Nodegraph *ptr, KmerMinHash *optr);

Nodegraph *nodegraph_with_tables(uintptr_t ksize, uintptr_t starting_size, uintptr_t n_tables);

void signature_add_sequence(Signature *ptr, const char *sequence, bool force);

void signature_add_protein(Signature *ptr, const char *sequence);

bool signature_eq(Signature *ptr, Signature *other);

KmerMinHash *signature_first_mh(Signature *ptr);

void signature_free(Signature *ptr);

Signature *signature_from_params(ComputeParameters *params);

SourmashStr signature_get_filename(Signature *ptr);

SourmashStr signature_get_license(Signature *ptr);

KmerMinHash **signature_get_mhs(Signature *ptr, uintptr_t *size);

SourmashStr signature_get_name(Signature *ptr);

uintptr_t signature_len(Signature *ptr);

Signature *signature_new(void);

void signature_push_mh(Signature *ptr, const KmerMinHash *other);

SourmashStr signature_save_json(Signature *ptr);

void signature_set_filename(Signature *ptr, const char *name);

void signature_set_mh(Signature *ptr, const KmerMinHash *other);

void signature_set_name(Signature *ptr, const char *name);

Signature **signatures_load_buffer(const char *ptr,
                                   uintptr_t insize,
                                   bool _ignore_md5sum,
                                   uintptr_t ksize,
                                   const char *select_moltype,
                                   uintptr_t *size);

Signature **signatures_load_path(const char *ptr,
                                 bool _ignore_md5sum,
                                 uintptr_t ksize,
                                 const char *select_moltype,
                                 uintptr_t *size);

uint8_t *signatures_save_buffer(Signature **ptr, uintptr_t size, uint8_t compression, uintptr_t *osize);

char sourmash_aa_to_dayhoff(char aa);

char sourmash_aa_to_hp(char aa);

/**
 * Clears the last error.
 */
void sourmash_err_clear(void);

/**
 * Returns the panic information as string.
 */
SourmashStr sourmash_err_get_backtrace(void);

/**
 * Returns the last error code.
 *
 * If there is no error, 0 is returned.
 */
SourmashErrorCode sourmash_err_get_last_code(void);

/**
 * Returns the last error message.
 *
 * If there is no error an empty string is returned.  This allocates new memory
 * that needs to be freed with `sourmash_str_free`.
 */
SourmashStr sourmash_err_get_last_message(void);

/**
 * Initializes the library
 */
void sourmash_init(void);

/**
 * Frees a sourmash str.
 *
 * If the string is marked as not owned then this function does not
 * do anything.
 */
void sourmash_str_free(SourmashStr *s);

/**
 * Creates a sourmash str from a c string.
 *
 * This sets the string to owned.  In case it's not owned you either have
 * to make sure you are not freeing the memory or you need to set the
 * owned flag to false.
 */
SourmashStr sourmash_str_from_cstr(const char *s);

char sourmash_translate_codon(const char *codon);

#endif /* SOURMASH_H_INCLUDED */
